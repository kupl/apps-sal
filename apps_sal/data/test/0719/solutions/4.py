# int(input())
# [int(i) for i in input().split()]

def gen(x, digits, summ):

    if summ < 0:
        return
    if digits == 1:
        if summ < 10:
            a.append(x * 10 + summ)
        return

    if x != 0:
        gen(x * 10, digits - 1, summ)
    for d in range(1, 10):
        gen(x * 10 + d, digits - 1, summ - d)


a = []
for digits in range(2, 9):
    gen(0, digits, 10)

a.sort()
k = int(input())
print(a[k - 1])
