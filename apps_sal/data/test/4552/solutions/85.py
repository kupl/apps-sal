def bitcount(x):
    x = x - (x >> 1 & 6148914691236517205)
    x = (x & 3689348814741910323) + (x >> 2 & 3689348814741910323)
    x = x + (x >> 4) & 1085102592571150095
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 127


def binary_to_int(x):
    temp = 0
    for i in range(len(str(x))):
        temp += 2 ** (len(str(x)) - i - 1) * int(str(x[i]))
    return temp


n = int(input())
shops = []
for i in range(n):
    shops.append(binary_to_int(''.join(input().split())))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, 2 ** 10):
    temp = 0
    for j in range(n):
        temp += p[j - 1][bitcount(i & shops[j - 1])]
    if i == 1:
        ans = temp
    elif temp > ans:
        ans = temp
print(ans)
