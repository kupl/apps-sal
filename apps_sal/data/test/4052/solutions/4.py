n = int(input())
s = input()
t = input()
t1 = True
ans = []
for i in range(n):
    if s[i] != t[i]:
        t2 = False
        y = []
        y.append(i + 1)
        for j in range(i + 1, n):
            if s[j] == t[i]:
                t2 = True
                x = j
                break
            y.append(1 + j)
        if t2:
            y = y[::-1]
            ans += y
            s = s[0:i] + t[i] + s[i:j] + s[j + 1:]
        else:
            t1 = False
            break
if t1:
    print(len(ans))
    for i in ans:
        print(i, end=' ')
else:
    print(-1)
