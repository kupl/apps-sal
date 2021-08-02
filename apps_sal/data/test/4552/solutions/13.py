n = int(input())
F = [int("".join(input().split()), 2) for _ in range(n)]
P = [list(map(int, input().split())) for _ in range(n)]
num = 1 << 10
ans = -(10 ** 10)


def popcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


# print(F)

for i in range(1, num):
    temp = 0
    for j in range(n):
        temp += P[j][popcnt(i & F[j])]
    ans = max(temp, ans)
print(ans)
