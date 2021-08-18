n, k = list(map(int, input().split()))
s = input()
A = [0 for i in range(26)]
for i in s:
    A[ord(i) - 65] += 1
A.sort()
i = 25
ans = 0
while k > 0:
    k -= A[i]
    ans += A[i] * A[i]
    i -= 1
if k < 0:
    k += A[i + 1]
    ans -= A[i + 1] * A[i + 1]
    ans += k * k

print(ans)
