s = input()
l = [0] * 26
ans = True
for ch in s:
    x = ord(ch) - ord('a')
    l[x] += 1
    for i in range(0, x):
        if l[i] == 0:
            ans = False
            break
if ans:
    for i in range(0, 26):
        if l[i] == 0:
            for j in range(i + 1, 26):
                if l[j] > 0:
                    ans = False
                    break
            break
if ans:
    print('YES')
else:
    print('NO')
