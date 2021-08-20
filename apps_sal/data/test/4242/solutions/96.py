(a, b, k) = map(int, input().split())
a_divisor = []
ab_divisor = []
for i in range(1, a + 1):
    if a % i == 0:
        a_divisor.append(i)
for j in a_divisor:
    if b % j == 0:
        ab_divisor.append(j)
print(ab_divisor[-k])
