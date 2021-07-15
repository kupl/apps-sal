n, x = list(map(int, input().split()))

l = list(map(int, input().split()))
ans = 1
p = 0
for i in range(n):
    p += l[i]
    if (p > x):
        break
    else:
        ans += 1

print(ans)

