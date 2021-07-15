s = input()
# print(s)
n: int = 0
odds = ""


for i in s:
    if n % 2 == 0:
        odd = s[n]
        odds += odd
    elif n == 0:
        odd = s[n]
        odds += odd
    else:
        pass
    n += 1
    # nを奇数にする
print(odds)
