n, d = list(map(int, input().split()))
s = input()
i = 0
i2 = 0
res = 0
while i != n - 1:
    i2 = i + d
    while i2 != i:
        if i2 < len(s) and s[i2] == "1":
            break
        i2 -= 1
    else:
        print(-1)
        break
    i = i2
    res += 1
else:
    print(res)
