a, b = map(int, input().split())


def xor(x):
    num = [0 for i in range(41)]
    for i in range(41):
        temp = (x + 1) // (2 ** (i + 1))
        temp2 = (x + 1) % (2 ** (i + 1))
        num[i] += temp * (2 ** i)
        num[i] += max(temp2 - 2 ** i, 0)
    return num


temp = [0 for i in range(41)]
temp2 = xor(b)
temp3 = xor(a - 1)
for i in range(41):
    temp[i] += temp3[i]
    temp[i] -= temp2[i]
    temp[i] %= 2
ans = 0
for i in range(41):
    ans += temp[i] * 2 ** i
print(ans)
