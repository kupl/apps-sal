n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
now = []
for i in range(n):
    now.append([a[i] - b[i], a[i], b[i]])
now.sort()
ans = 0
i = 0
j = n - 1
while i < j:
    if now[i][0] + now[j][0] > 0:
        ans += j - i
        j -= 1
    else:
        i += 1
print(ans)

