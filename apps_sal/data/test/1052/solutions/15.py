from math import factorial as f
n, k = list(map(int, input().split()))

an = 0
dr = [0, 0, 1, 2, 9]
for i in range(n - k, n + 1):
    r = n - i
    if r == 0:
        an += 1
    elif r != 1:
        an += dr[r] * f(n) // (f(i) * f(n - i))
print(an)
