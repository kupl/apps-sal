n = int(input())
s = set()
x = n
s.add(x)
ans = 0
while 1:
    x = x + 1
    while x % 10 == 0:
        x //= 10
    if x in s:
        break
    else:
        s.add(x)
        ans += 1
print(len(s))
