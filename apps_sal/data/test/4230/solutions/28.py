(x, n) = list(map(int, input().split()))
p = sorted(list(map(int, input().split())))
a = 100
b = 0
for i in range(0, 102):
    if i not in p and abs(x - i) < a:
        a = abs(x - i)
        b = i
print(b)
