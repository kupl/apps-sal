s = input()
n = len(s)
i = k = p = 1
while i < n:
    while i < n and int(s[i]) + int(s[i - 1]) == 9:
        k += 1
        i += 1
    if k % 2 != 0:
        p *= (k + 1) // 2
    k = 1
    i += 1
print(p)
