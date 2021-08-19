(a, b) = map(int, input().split())
c = b - a
tmp = 0
for i in range(1, c + 1):
    tmp += i
print(tmp - b)
