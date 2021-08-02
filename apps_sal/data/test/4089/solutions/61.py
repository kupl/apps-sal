n = int(input())
ans = list()
x = ord("a")
while n > 0:
    n -= 1
    ans.append(chr(x + n % 26))
    n //= 26
print(("".join(ans[::-1])))
