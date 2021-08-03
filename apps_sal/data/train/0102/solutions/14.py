t = int(input())
ans = []
for j in range(t):
    n = int(input())
    s = ''
    k = 0
    for i in range(1, 10):
        s = str(i)
        while int(s) <= n:
            k += 1
            s += str(i)
    ans.append(k)
for i in ans:
    print(i)
