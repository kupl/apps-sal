n, m = list(map(int, input().split()))
for i in range(m):
    a = list(map(int, input().split()))
    s = set()
    for i in range(1, len(a)):
        s.add(a[i])
    k = list(s)
    isok = 0
    for i in range(len(k)):
        if -k[i] in s:
            isok = 1
    if not isok:
        print("YES")
        return
print("NO")
