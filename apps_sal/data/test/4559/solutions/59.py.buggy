n = int(input())
l = list(map(int, input().split()))
m = 1
l.sort()
for i in range(n):
    m *= l[i]
    if m > 10**18:
        print(-1)
        return

print(m)
