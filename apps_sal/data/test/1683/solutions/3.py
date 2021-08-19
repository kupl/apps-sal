n = int(input())
mod = 998244353
ans = 0
ai = input().split()
lengths = [0] * 11
for i in range(n):
    temp = len(ai[i])
    lengths[temp] += 1
tens = [0] * 25
for i in range(25):
    tens[i] = 10 ** i
for i in range(n):
    temp = len(ai[i])
    num = 0
    for j in range(temp, 11):
        num += lengths[j]
    for z in range(temp):
        ans += num * tens[z * 2] * int(ai[i][-z - 1])
        ans += num * tens[z * 2 + 1] * int(ai[i][-z - 1])
    for j in range(1, temp):
        if lengths[j] != 0:
            for z in range(j):
                ans += lengths[j] * tens[z * 2] * int(ai[i][-z - 1])
                ans += lengths[j] * tens[z * 2 + 1] * int(ai[i][-z - 1])
            for z in range(temp - j):
                ans += 2 * lengths[j] * tens[j * 2 + z] * int(ai[i][-(z + j) - 1])
    ans %= mod
print(ans)
