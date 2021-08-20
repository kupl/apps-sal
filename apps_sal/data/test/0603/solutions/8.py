string = input()
m = string.index(' ')
n = string[m + 1:].index(' ') + m + 1
r = int(string[:m])
g = int(string[m:n])
b = int(string[n:])
if r == 0 and g % 3 == 2 and (b % 3 == 2) or (b == 0 and g % 3 == 2 and (r % 3 == 2)) or (g == 0 and r % 3 == 2 and (b % 3 == 2)):
    print(r // 3 + g // 3 + b // 3)
elif r % 3 == g % 3 or r % 3 == b % 3 or b % 3 == g % 3:
    print((r + b + g) // 3)
else:
    print((r + b + g) // 3 - 1)
