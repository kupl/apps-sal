s = input().strip()
n = len(s)
i = j = k = 0
while i < n:
    j = i
    i += 1
    while i < n and s[i] == '0':
        i += 1
    if j > i - j:
        k += 1
    elif j == i - j:
        if s[:j] >= s[j:i]:
            k += 1
        else:
            k = 0
    else:
        k = 0
print(k + 1)
