k = int(input())
a = []
for i in range(1, 10):
    for i1 in range(1, 10):
        a.append(str(i) * i1)
for _ in range(k):
    n = int(input())
    ans = 0
    for i1 in a:
        if int(i1) <= n:
            ans += 1
    print(ans)
