t = int(input())

s = [10 ** i - 1 for i in range(1, 18)]

for _ in range(t):
    a, b = map(int, input().split())
    c = 0
    for i in s:
        if i <= b:
            c += 1
        else:
            break
    print(a * c)
