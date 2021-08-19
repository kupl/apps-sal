str = input()
if len(str) >= 2:
    n = int(str[-2] + str[-1])
elif len(str) == 1:
    n = int(str[0])
a2 = [1, 2, 4, 3]
a3 = [1, 3, 4, 2]
a4 = [1, 4]
print((1 + a2[n % 4] + a3[n % 4] + a4[n % 2]) % 5)
