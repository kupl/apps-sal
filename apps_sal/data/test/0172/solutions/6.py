n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ax = [0, 0, 0, 0, 0, 0]
bx = [0, 0, 0, 0, 0, 0]
for i in range(n):
    ax[a[i]] += 1
    bx[b[i]] += 1
ans = 0
for i in range(6):
    if (ax[i] + bx[i]) % 2 == 1:
        ans = -1
        break
    else:
        ans += abs((ax[i] - bx[i]) // 2)
print(ans // 2)
