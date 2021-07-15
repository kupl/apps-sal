n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

ans = 0
for i in range(n):
    ans += a[2*i+1]
print(ans)

