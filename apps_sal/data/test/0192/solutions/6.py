s = input()
x = int(s.split()[0])
y = int(s.split()[1])
a = [0] * 25
a[0] = y
a[1] = 2 * y - 1
ans = 0
for i in range(2, 25):
    if x <= a[i - 1]:
        ans = i + 1
        break
    a[i] = a[i - 1] + a[i - 2] - 1
print(ans)

