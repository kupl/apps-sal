num = int(input(''))
ans = 0
if num / 500 > 0:
    ans += int(num / 500) * 1000
    num = num % 500
if num / 5 > 0:
    ans += int(num / 5) * 5
    num /= 5
print(ans)
