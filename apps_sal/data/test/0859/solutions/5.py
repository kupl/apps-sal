
def factorial(n):
    i = 1
    for j in range(1, n + 1):
        i *= j
    return i


def choose(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))


l = list(input())
exp = 0
for i in range(len(l)):
    if l[i] == "+":
        exp += 1
    else:
        exp -= 1

l1 = list(input())
dis = 0
unrec = 0
for i in range(len(l1)):
    if l1[i] == "+":
        dis += 1
    elif l1[i] == "-":
        dis -= 1
    else:
        unrec += 1


if abs(exp - dis) > unrec:
    print(0)
elif unrec == 0:
    print(1)
else:
    print(choose(unrec, (abs(exp - dis) + int((unrec - abs(exp - dis)) / 2))) / 2**unrec)
