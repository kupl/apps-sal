t = int(input())
ans = []
for _ in range(t):
    s = input()
    p = []
    i = 0
    n = len(s)
    while (i+3<=n):
        if (i+5<=n) and (s[i:i+5]=='twone'):
            p.append(i+3)
            i+=5
        elif (s[i:i+3]=='one'):
            p.append(i+2)
            i+=3
        elif (s[i:i+3]=='two'):
            p.append(i+2)
            i+=3
        else:
            i+=1
    ans.append(p.copy())

for a in ans:
    print(len(a))
    print(' '.join(list(map(str, a))))
