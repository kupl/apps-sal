s = input()
plus = 0
minus = 0
seen = 0
for letter in s:
    if letter == '+':
        if minus == 0:
            plus += 1
            seen += 1
        else:
            plus += 1
            minus -= 1
    elif plus == 0:
        minus += 1
        seen += 1
    else:
        minus += 1
        plus -= 1
print(seen)
