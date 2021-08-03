s = input()
a, b = [int(x) for x in s.split()]
c, ans = 0, 0
while True:
    c = min(a, b)
    a = max(a, b)
    b = c
    ans += a // b
    a = a % b
    if a % b == 0:
        break
print(ans)
