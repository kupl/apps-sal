q = int(input())
for _ in range(q):
    s = input()
    n = len(s)
    ans = 100000000
    r = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if(s[i] == '1'):
            ans = i
        r[i] = ans
    ansss = 0
    for i in range(n):
        ns = 0
        for j in range(r[i], n):
            ns = 2 * ns + (ord(s[j]) - ord('0'))
            if(ns == j - i + 1):
                ansss += 1
            if(ns > n):
                break
    print(ansss)
