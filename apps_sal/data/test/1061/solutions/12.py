a = []
for i in range(5):
    a.extend(map(int, input().split()))
a = a.index(1)
print(abs(a // 5 - 2) + abs(a % 5 - 2))
