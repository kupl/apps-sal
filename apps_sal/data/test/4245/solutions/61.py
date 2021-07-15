a, b = map(int, input().split())
num = 1
c = 0
while num < b:
    num += a-1
    c += 1
print(c)
