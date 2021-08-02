n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = [0] * 6
b1 = [0] * 6
for i in a:
    a1[i] += 1
for i in b:
    b1[i] += 1
ans = 0
for i in range(1, 6):
    if (a1[i] + b1[i]) % 2 != 0:
        ans = -1
        break
    ans += (max(a1[i], b1[i]) - min(a1[i], b1[i])) // 2
if ans == -1:
    print(-1)
else:
    print(ans // 2)
