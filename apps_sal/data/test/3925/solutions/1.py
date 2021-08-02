s = input()
n = len(s)

s = s + s + s

max = cur = 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        cur += 1
        if max < cur:
            max = cur
    else:
        cur = 1

if max > n:
    print(n)
else:
    print(max)
