import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
for A_i, A_j in itertools.combinations(A, r=2):
    ans = max(ans, abs(A_i - A_j))

print(ans)
