def inpl():
    return list(map(int, input().split()))


N = int(input())
A = inpl() + [-1]
x = max(A)
ctr = 0
ans = 0
for a in A:
    if a == x:
        ctr += 1
    else:
        ans = max(ans, ctr)
        ctr = 0
print(ans)
