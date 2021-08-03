t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    s = input()
    n = len(s)
    l = []
    start = 0
    end = 0
    done = 0
    for i in range(n):
        if(done):
            if(s[i] == '1'):
                end += 1
            else:
                l.append((start, end))
                done = 0
        else:
            if(s[i] == '1'):
                done = 1
                start = i
                end = i
    if(done):
        l.append((start, end))
    z = a * len(l)
    lo = []
    for i in range(len(l) - 1):
        lo.append(l[i + 1][0] - l[i][1] - 1)
    for i in lo:
        if(i * b < a):
            z -= a
            z += (i * b)
    print(z)
