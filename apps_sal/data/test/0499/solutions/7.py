n = int(input())
s = input()
t = 'BGR'
a = [s.count(c) for c in t]
ans = ''
for i in range(3):
    (x, y, z) = (a[i], a[(i + 1) % 3], a[(i + 2) % 3])
    if x >= 1 and y == z == 0 or (y >= 1 and z >= 1) or (x >= 1 and (y >= 2 or z >= 2)):
        ans += t[i]
print(ans)
