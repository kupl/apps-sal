n = int(input())
As = list(map(int, input().split()))
for i in range(n):
    As[i] = As[i] - i
As = sorted(As)
b1 = As[n // 2]
if n % 2 == 0:
    b2 = As[(n - 1) // 2]
else:
    b2 = As[n // 2]
ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += abs(b1 - As[i])
    ans2 += abs(b2 - As[i])
print(min(ans1, ans2))
