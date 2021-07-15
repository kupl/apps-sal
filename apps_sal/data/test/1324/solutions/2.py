a = list(map(int, input().split()))
s = input().strip()
ans = 0
for i in s:
    ans += a[int(i) - 1]
    
print(ans)

