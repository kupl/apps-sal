s = int(input())
r = 0
for i in [100, 20, 10, 5, 1]:
    r += s // i
    s %= i
print(r)
