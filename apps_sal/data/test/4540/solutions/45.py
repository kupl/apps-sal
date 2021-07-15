n = int(input())
a = [0] + list(map(int,input().split())) + [0]
c = []
total = 0
for i in range(n+1):
    tmp = abs(a[i+1] - a[i])
    c.append(tmp)
    total += tmp
    
for i in range(1,n+1):
    ans = total - c[i-1] - c[i] + abs(a[i+1] - a[i-1])
    print(ans)
