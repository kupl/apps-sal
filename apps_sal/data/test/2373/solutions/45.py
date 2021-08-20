n = int(input())
pp = list(map(int, input().split()))
cnt = 0
for i in range(n - 1):
    if pp[i] == i + 1:
        (pp[i], pp[i + 1]) = (pp[i + 1], pp[i])
        cnt += 1
if pp[-1] == n:
    cnt += 1
print(cnt)
