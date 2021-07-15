t = int(input())
a = []
for i in range(t):
    n = int(input())
    a.append(n)
for i in range(t):
    ans = 0
    for j in range(1, 10):
        for k in range(1, 10):
            if int(str(j) * k) <= a[i]:
                ans += 1
    print(ans)
