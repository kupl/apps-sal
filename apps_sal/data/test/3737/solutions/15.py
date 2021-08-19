n = int(input())
a = list(map(int, input().split()))
minim = min(a)
maxim = max(a)
ans = 0
for i in a:
    if minim < i < maxim:
        ans += 1
print(ans)
