n = int(input())
ans = list()
x = ord("a")
while n > 0:
    y = n % 26
    if y == 0:
        y = 26
    y -= 1
    ans.append(chr(x + y))
    n -= y
    n //= 26
print(("".join(ans[::-1])))

