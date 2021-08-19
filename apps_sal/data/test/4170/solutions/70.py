a = int(input())
f = list(map(int, input().split()))
count = 0
ma = 0
ans = {}
for i in range(len(f) - 1):
    if f[i + 1] <= f[i]:
        count += 1
    else:
        ma = max(ma, count)
        count = 0
if count >= 1:
    ma = max(ma, count)
print(ma)
