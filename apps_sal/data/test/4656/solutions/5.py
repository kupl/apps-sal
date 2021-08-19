import math
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    s = input()
    slist = []
    for i in range(n):
        slist.append(s[i])
    slist.sort()
    slist2 = []
    slist2.append([slist[0], 1])
    for i in range(1, len(s)):
        if slist2[-1][0] == slist[i]:
            slist2[-1][1] += 1
        else:
            slist2.append([slist[i], 1])
    maxans = 1
    for i in range(2, n + 1):
        b = math.gcd(i, k)
        a = i // b
        while (a + 1) * b <= i:
            a += 1
        temp = 0
        for j in range(len(slist2)):
            c = slist2[j][1] // a
            while (c + 1) * a <= slist2[j][1]:
                c += 1
            temp += c
        if temp >= b:
            maxans = i
    print(maxans)
