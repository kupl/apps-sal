n, p = list(map(int, input().split()))
a = list(map(int, input().split()))

num = [0] * (5001)
for i in a:
    num[i] += 1

for i in range(5000):
    num[i + 1] += num[i]

ans = []

for x in range(1, 2001):

    temp = 1
    candy = x
    for i in range(x, x + n):
        temp *= num[candy] - (i - x)
        temp %= p
        candy += 1

    if temp % p != 0:
        ans.append(x)

print(len(ans))
print(*ans)
