n = int(input())
a = list(map(int, input().split()))
i = 0
while i + 1 < n and a[i] < a[i + 1]:
    i += 1
j = n - 1
while j > 0 and a[j] < a[j - 1]:
    j -= 1
flag = True
for x in range(i, j + 1):
    if a[x] != a[i]:
        flag = False
        break
print("YES" if flag else "NO")

