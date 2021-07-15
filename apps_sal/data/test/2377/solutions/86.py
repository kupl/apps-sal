from math import ceil
n,h = map(int,input().split())
k = [list(map(int,input().split())) for i in range(n)]
a,b = [list(i) for i in zip(*k)]
b.sort(reverse=True)
a = max(a)
ans = 0
for i in b:
    if i > a:
        ans += 1
        h -= i
        if h <= 0:
            print(ans)
            return
    else:
        break
print(ans + ceil(h / a))
