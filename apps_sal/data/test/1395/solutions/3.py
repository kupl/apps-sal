s = input()
m = int(input())
N = int(s)
MIN = N % m
L = len(s) - 1
temp1 = N
temp2 = 0
big = pow(10, L, m)
for i in range(0, len(s) - 1):
    temp2 *= 10
    temp2 += int(s[i])
    temp2 %= m
    temp1 -= big * int(s[i])
    temp1 *= 10
    temp1 %= m
    temp = temp1 + temp2
    temp %= m
    if s[i + 1] != '0':
        if temp < MIN:
            MIN = temp
print(MIN)
