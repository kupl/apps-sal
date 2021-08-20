n = int(input())
F = [int(''.join(input().split()), 2) for _ in range(n)]
P = [list(map(int, input().split())) for _ in range(n)]
num = 1 << 10
ans = -10 ** 10


def popcnt(n):
    c = (n & 6148914691236517205) + (n >> 1 & 6148914691236517205)
    c = (c & 3689348814741910323) + (c >> 2 & 3689348814741910323)
    c = (c & 1085102592571150095) + (c >> 4 & 1085102592571150095)
    c = (c & 71777214294589695) + (c >> 8 & 71777214294589695)
    c = (c & 281470681808895) + (c >> 16 & 281470681808895)
    c = (c & 4294967295) + (c >> 32 & 4294967295)
    return c


for i in range(1, num):
    temp = 0
    for j in range(n):
        temp += P[j][popcnt(i & F[j])]
    ans = max(temp, ans)
print(ans)
