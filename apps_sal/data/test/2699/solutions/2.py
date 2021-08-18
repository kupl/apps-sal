def first_row(n):
    l = [1]
    s = [2]
    t = [4]
    f = [3]
    d = 3
    for i in range(n - 1):
        l.append(l[-1] + d)
        s.append(l[-1] + 1)
        t.append(s[-1] * 2)
        f.append(s[-1] + 1)
        d = d * 2
    for i in range(len(l)):
        print(l[i], end=" ")
    print("")
    for i in range(len(s)):
        print(s[i], end=" ")
    print("")
    for i in range(len(t)):
        print(t[i], end=" ")
    print("")
    for i in range(len(f)):
        print(f[i], end=" ")
    print("")


t = int(input())
l = list(map(int, input().split()))
for i in range(len(l)):
    first_row(l[i])
