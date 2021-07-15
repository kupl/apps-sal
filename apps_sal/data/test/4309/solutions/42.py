n = int(input())

for i in range(n, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    if a == b == c:
        print(i)
        return

