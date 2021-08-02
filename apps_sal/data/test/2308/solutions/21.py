t = int(input())
for l in range(t):
    a = str(input())
    b = str(input())
    a = a[::-1]
    b = b[::-1]
    s1 = -1
    for i in range(len(b)):
        if(b[i] == '1'):
            s1 = i
            break
    if(s1 == -1):
        print(0)
    else:
        ans = 0
        for j in range(len(a)):
            if(a[j] == '1' and j >= i):
                ans = j - i
                break
        print(ans)
