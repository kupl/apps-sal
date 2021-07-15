h1, m1 = list(map(int,input().split(":")))
h2, m2 = list(map(int,input().split(":")))
num = h1 * 60 + m1 + h2 * 60 + m2
num //= 2
num2 = str(num // 60)
num3 = str(num % 60)
if len(num2) == 1:
    num2 = "0"+ num2
if len(num3) == 1:
    num3 = "0"+ num3
print(num2+ ":" + num3)

