size = 1001
n = int(input())
a = [0] * size
ans = 0
num = map(int, input().split())
for b in num:
    a[b] += 1

while a.count(0) != size:
    cnt = 0
    for i in range(size):
        if a[i]:
            cnt += 1
            a[i] -= 1
    ans += cnt - 1

print(ans)
