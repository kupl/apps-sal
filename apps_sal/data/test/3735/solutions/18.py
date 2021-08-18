

n = input()
x = len(n)

if x >= 2:
    m1 = int("9" * (x - 1))
else:
    m1 = 0
m2 = int(n) - m1

ANS = 0
for i in str(m1) + str(m2):
    ANS += int(i)

print(ANS)
