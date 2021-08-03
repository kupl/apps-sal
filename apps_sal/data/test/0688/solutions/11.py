num = input()
str = input()
d = dict()
used = dict()
num = num.replace('5', '2')
str = str.replace('5', '2')
num = num.replace('9', '6')
str = str.replace('9', '6')
res = 10 ** 1000
for i in num:
    res = min(res, str.count(i) // num.count(i))
print(res)
