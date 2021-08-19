N = int(input())
A = [int(x) for x in input().split()]
counter = {}
for i in range(N):
    counter[i + A[i]] = 0
ans = 0
for i in range(N):
    if i - A[i] in counter:
        ans += counter[i - A[i]]
    counter[i + A[i]] += 1
print(ans)
