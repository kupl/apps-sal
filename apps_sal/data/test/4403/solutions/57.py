S = list(input())
num = 0
for s in S:
    if s == "+":
        num += 1
    else:
        num -= 1
print(num)
