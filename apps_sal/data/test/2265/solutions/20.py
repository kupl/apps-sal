(a, b, res) = (input(), input(), 0)
sm1 = sum(map(int, b[0:len(b)]))
sm2 = sum(map(int, a[0:len(b)]))
res += (sm1 - sm2) % 2 == 0
for i in range(len(b), len(a)):
    sm2 += a[i] == '1'
    sm2 -= a[i - len(b)] == '1'
    res += (sm1 - sm2) % 2 == 0
print(res)
