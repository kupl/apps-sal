n = int(input())
a = list(map(int, input().split()))
f = 'YES'
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) > 1:
        f = 'NO'
        break
print(f)
