ans = 0
a = [4, 1, 3, 2, 0, 5]
x = int(input())
for i in range(6):
    if x & 1 << i:
        ans += 1 << a[i]
print(ans)
