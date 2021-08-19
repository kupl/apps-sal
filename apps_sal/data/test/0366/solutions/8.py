(n, s) = map(int, input().split())
x = s // n
if x * n < s:
    x += 1
print(x)
