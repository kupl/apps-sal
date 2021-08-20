h = input()
c = (h.count('B'), h.count('S'), h.count('C'))
n = list(map(int, input().split()))
p = list(map(int, input().split()))
r = int(input())
(a, b) = (0, 10 ** 15)
while a + 1 < b:
    x = (a + b) // 2
    y = sum((max(0, x * c[i] - n[i]) * p[i] for i in range(3)))
    if y <= r:
        a = x
    else:
        b = x
print(a)
