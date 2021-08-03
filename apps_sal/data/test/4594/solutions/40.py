n = int(input())
d = [int(input()) for i in range(n)]
d = sorted(d, reverse=True)
ans = 0
last = 101
for i in d:
    if i < last:
        ans += 1
        last = i
print(ans)
