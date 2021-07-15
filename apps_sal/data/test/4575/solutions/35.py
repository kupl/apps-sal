n = int(input())
d,x = map(int, input().split())
a = list(int(input()) for _ in range(n))
ans = 0
for i in range(n):
    p = (a[i]+1)-1
    ans += 1 + (d-1)//p
print(ans+x)
