n = int(input())
a, b = 0, 0
for i in range(n):
    s = [j for j in input().split()]
    if s[1] == 'soft':
        a += 1
    else:
        b += 1
for i in range(1, 100):
    if i % 2 == 0:
        k = i * i
        if k // 2 >= a and k // 2 >= b:
            print(i)
            return
    else:
        k = i * i
        k //= 2
        if k + 1 >= max(a, b) and k >= min(a, b):
            print(i)
            return
