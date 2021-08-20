from fractions import Fraction
S = int(input())
l = S // 3
c = 1
count = 1
if S < 3:
    count = 0
for i in range(1, l):
    c = Fraction(c * (S - 3 * i) * (S - 3 * i - 1) * (S - 3 * i - 2), (S - 2 * i - 1) * (S - 2 * i - 2) * i)
    count += c
answer = int(count) % (10 ** 9 + 7)
print(answer)
