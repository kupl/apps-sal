n = int(input())
for i in range(n):
    q = int(input())
    l = list(map(int, input().split()))
    a = 0
    b = 0
    c = 0
    for i in range(q):
        if(l[i] % 3 == 0):
            a += 1
        elif(l[i] % 3 == 1):
            b += 1
        else:
            c += 1
    print(a + min(c, b) + (max(c, b) - min(c, b)) // 3)
