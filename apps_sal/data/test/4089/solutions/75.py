n = int(input())
ans = ""
for i in range(14):
    if n == 0:
        break
    else:
        n -= 1
        ans += chr(ord("a") + n % 26)
        n = n // 26

rslt = ans[::-1]
print(rslt)
