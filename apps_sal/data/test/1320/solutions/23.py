n = int(input())

rows = [0] * n
cols = [0] * n

def fact(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res

def nC2(count):
    if count < 2:
        return 0
    elif count == 2:
        return 1
    return fact(count)//(2*fact(count-2))

for row in range(n):
    for col, ch in enumerate(input()):
        if ch == "C":
            rows[row] += 1
            cols[col] += 1

res = sum((nC2(num) for num in rows)) + sum((nC2(num) for num in cols))
print(res)

