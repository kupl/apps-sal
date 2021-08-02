t = int(input())
for i in range(t):
    s = list(input())
    if len(set(s)) == 1:
        print(-1)
    else:
        s.sort()
        a = ''
        for i in s:
            a += i
        print(a)
