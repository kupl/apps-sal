n = int(input())
s = input()
summ = 0
for i in range(n):
    summ += int(s[i])
for i in range(2, 101):
    if summ % i == 0:
        d = 0
        for j in range(n):
            d += int(s[j])
            if d * i == summ:
                d = 0
            if d * i > summ:
                break
        if (j == n - 1 and d == 0):
            print('YES')
            return
print('NO')
