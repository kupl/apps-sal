k = int(input())
s = input()
t = input()
num = [0] * k
num2 = [0] * k
alth = 'abcdefghijklmnopqrstuvwxyz'
for i in range(k):
    num[i] = alth.find(s[i])
    num2[i] = alth.find(t[i])
num3 = [0] * k
rem = 0
for i in range(k - 1, -1, -1):
    num3[i] = num2[i] - num[i] - rem
    if num3[i] < 0:
        num3[i] += 26
        rem = 1
    else:
        rem = 0
rem = 0
j = 0
while j < k:
    rem2 = (num3[j] + rem) % 2
    num3[j] = (num3[j] + rem) // 2
    rem = 26 * rem2
    j += 1
rem = 0
for i in range(k - 1, -1, -1):
    num[i] += num3[i] + rem
    if num[i] > 25:
        num[i] -= 26
        rem = 1
    else:
        rem = 0
for i in num:
    print(alth[i], end='')
