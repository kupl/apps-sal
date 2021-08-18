a = int(input())
b = int(input())
n = a + b + 1
ans = [i for i in range(1, n + 1)]

if b % 2 == 1:
    ans[n // 2 - 1] = ans[n // 2 - 1] + ans[n // 2]
    ans[n // 2] = ans[n // 2 - 1] - ans[n // 2]
    ans[n // 2 - 1] = ans[n // 2 - 1] - ans[n // 2]
    b -= 1

left = 0
right = n - 1

while b > 0:
    ans[left] = ans[left] + ans[right]
    ans[right] = ans[left] - ans[right]
    ans[left] = ans[left] - ans[right]
    left += 1
    right -= 1
    b -= 2

for i in range(n - 1):
    print(ans[i], end=' ')
print(ans[n - 1])
