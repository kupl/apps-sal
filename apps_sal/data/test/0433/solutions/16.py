n, a, b = list(map(int, input().split()))
s = (a + b) % n
if s == 0:
    s = n
print(s)
