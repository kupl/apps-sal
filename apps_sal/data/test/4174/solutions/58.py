n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
count = 1
for i in range(n):
    ans += l[i]
    if ans <= x:
        count += 1
print(count)
