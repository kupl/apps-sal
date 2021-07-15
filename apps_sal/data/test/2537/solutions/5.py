q = int(input())
alth = "qwertyuiopasdfghjklzxcvbnm"
for i in range(q):
    s = input()
    t = input()
    p = input()
    s1 = [0] * 26
    p1 = [0] * 26
    t1 = [0] * 26

    for i in s:
        s1[alth.find(i)] += 1

    for i in p:
        p1[alth.find(i)] += 1

    for i in t:
        t1[alth.find(i)] += 1

    ans = 1
    for i in range(26):
        if s1[i] + p1[i] < t1[i]:
            ans = 0
            break
    if ans == 0:
        print("NO")
    else:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while i < n and j < m:
            if t[j] == s[i]:
                i += 1
            j += 1
        if i != n:
            ans = 0
        
        if ans == 0:
            print("NO")
        else:
            print("YES")

