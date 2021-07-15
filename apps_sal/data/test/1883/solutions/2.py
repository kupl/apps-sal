n = int(input())
a, b = [0] + list(map(int, input().split())), [0] + list(map(int, input().split()))
ans, p = [], [0] * (n + 1)
for i in b:
    p[i] += 1
for i in range(1, n + 1):
    if a[i] == 1:
        t = [i]
        x = b[i]
        while p[x] == 1:
            t.append(x)
            x = b[x]            
        if len(t) > len(ans): ans = t[:]
ans.reverse()
print(len(ans))
print(' '.join(str(x) for x in ans))
