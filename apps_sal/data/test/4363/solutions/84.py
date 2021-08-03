k, s = [int(x) for x in input().split()]

res = 0

for i in range(k + 1):
    for j in range(k + 1):
        cc = s - i - j
        if 0 <= cc <= k:
            res += 1

print(res)
