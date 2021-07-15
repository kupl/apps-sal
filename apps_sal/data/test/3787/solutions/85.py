n,a,b = map(int, input().split())
if a+b > n+1 or a*b < n:
    print(-1)
    return

l = []
used = 0
for i in range(a):
    tmp = []
    for j in range(b):
        tmp.append(used+1)
        used += 1
        if n-used == a-i-1:
            break
    l.extend(tmp[::-1])
print(*l)
