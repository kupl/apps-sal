x = int(input())
n = x // 11
n = 2 * n
m = x % 11
if 1 <= m <= 6:
    n += 1
elif 7 <= m <= 10:
    n += 2
print(n)
