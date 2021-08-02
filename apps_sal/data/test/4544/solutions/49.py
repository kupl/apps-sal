N = int(input())
A = list(map(int, input().split()))
co = [0 for i in range(100002)]

for i in A:
    co[i] += 1

ans = 0
for i in range(100001):
    if i == 0:
        x = co[0] + co[1]
    else:
        x = co[i - 1] + co[i] + co[i + 1]

    ans = max(ans, x)
print(ans)
