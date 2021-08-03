n = int(input())
d, x = map(int, input().split())
c = 0
for i in range(n):
    a = int(input())
    for j in range(100):
        if a * j + 1 <= d:
            c += 1
        else:
            break
print(x + c)
