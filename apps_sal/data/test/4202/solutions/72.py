L, R = map(int, input().split())


def mod(num):
    return num % 2019


ans = 10 ** 9

lr = min(R, L + 2019) + 1

for i in range(L, lr):
    for j in range(i + 1, lr):
        ans = min(ans, mod(i * j))

print(ans)
