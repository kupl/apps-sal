import sys
a, b, c = (int(i) for i in input().split(" "))
# print(a, b, c)


def calculate(a, b, c, s):
    # print("in calc", a,b,c,s)
    return b * (s ** a) + c


def dig_sum(x):
    # print(x)
    line = str(x).strip("-")
    sum = 0
    for i in list(line):
        sum += int(i)
    return sum


res = []
for i in range(1, 82):
    x = calculate(a, b, c, i)
    # print(x, dig_sum(x))
    if dig_sum(x) == i:
        res.append(x)

res.sort()
res = [str(i) for i in res if i >= 0 and i < 1000000000]
print(len(res))
print(" ".join(res))
return
