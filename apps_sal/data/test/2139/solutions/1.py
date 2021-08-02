s = input()
ans = 0
li = []
for i in range(len(s)):
    if s[i:i + 4] == 'bear':
        li.append(i)
if len(li) == 0:
    print(0)
else:
    k = 0
    start = li[k]
    b = 0
    for i in range(len(s)):
        while i > start:
            try:
                k += 1
                start = li[k]
            except:
                b = 1
                break
        if b:
            break
        ans += len(s) - start - 3

    print(ans)
