
n = int(input())
a = list(map(int, input().split()))
i = n - 1
while i + 1:
    if a[i] != a[-1]:
        break
    i -= 1
print(i + 2)
