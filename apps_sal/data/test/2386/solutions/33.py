n = int(input())
A = []
for i, a in enumerate(map(int, input().split()), 1):
    A.append(a-i)
A.sort()
b = A[n//2]
ans = 0
for a in A:
    ans += abs(a-b)
print(ans)

