import itertools

n, m, q = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(q)]

def check(A, Q):
    if A[Q[1]-1] - A[Q[0]-1] == Q[2]:
        return Q[3]
    else:
        return 0

ans = 0
for i in itertools.combinations_with_replacement(list(range(1, m+1)), n):
    tmp = 0
    for j in a:
        tmp += check(i, j)
    if ans < tmp:
        ans = tmp

print(ans)

