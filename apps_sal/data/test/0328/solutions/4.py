c = 0
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a + b > c:
        c = a + b
print(c)
