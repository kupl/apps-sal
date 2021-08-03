n = int(input())
a = list(int(input()) for _ in range(5))
Min = min(a)

if n <= Min:
    print(5)
    return

x = n // Min
if n % Min != 0:
    x += 1
print(4 - a.index(Min) + x + a.index(Min))
