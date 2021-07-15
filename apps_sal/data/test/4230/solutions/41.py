x, n = list(map(int, input().split()))
p = list(map(int, input().split()))
a = 101
b = 101
for i in range(x, 102):
    if i not in p:
        a = i
        b = i - x
        break
for i in range(x - 1, -101, -1):
    if a == x:
        break
    if i not in p:
        c = x - i
        if c <= b:
            a = i
            break
        else:
            break
print(a)

