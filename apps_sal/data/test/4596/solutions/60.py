n = int(input())
li = list(map(int, input().split()))
b = float('inf')
for a in li:
    c = 0
    while a % 2 == 0:
        a = a / 2
        c += 1
    b = min(b, c)
print(b)
