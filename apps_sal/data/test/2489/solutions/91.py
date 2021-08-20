N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
L = [0] * (A[-1] + 1)
for a in A:
    L[a] = 1
for p in A:
    if not L[p]:
        continue
    L[p] += 1
    n = 2
    while p * n <= A[-1]:
        L[p * n] = 0
        n += 1
ans = L.count(2)
print(ans)
