n = int(input())
ip = list(map(int, input().split()))
ans = 0
t = max(ip)
for i in ip:
    ans += t - i
print(ans)
