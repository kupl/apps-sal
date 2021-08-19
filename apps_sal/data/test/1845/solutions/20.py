def inpl():
    return list(map(int, input().split()))


N = int(input())
A = inpl()
A.sort()
ma = A[0]
ans = 0
for b in A[1:]:
    for x in range(1, b // 2 + 1):
        if b % x:
            continue
        ans = max(ans, ma + b - ma * x - b // x)
print(sum(A) - ans)
