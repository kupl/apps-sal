n = int(input())
l = list(map(int, input().split()))
l.append(-1)
count = 0
ans = 0
for i in range(n + 1):
    if l[i] >= 4:
        count += 1
    else:
        ans += count // 3
        count = 0
print(ans)
