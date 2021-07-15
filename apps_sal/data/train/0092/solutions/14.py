q = int(input())
for i in range(q):
    k = 0
    s = input()
    t = input()
    for p in range(len(s)):
        for j in range(len(s)):
            if s[p] == t[j]:
                k += 1
    if k > 0:
        print('YES')
    else:
        print('NO')
