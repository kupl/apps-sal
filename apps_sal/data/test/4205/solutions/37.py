a = int(input())
f = list(map(int, input().split()))

count = 0
for i in range(a - 1):
    if f[i] != f[i + 1] - 1:
        f[i + 1] = i + 2
        count += 1
if count == 2 or count == 0:
    print("YES")
else:
    print("NO")
