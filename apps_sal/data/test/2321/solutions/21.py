n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    num1 = 0
    num2 = 0
    j1 = 0
    j2 = m - 1
    while j1 < m and s[j1] == '<':
        num1 += 1
        j1 += 1
    while j2 >= 0 and s[j2] == '>':
        num2 += 1
        j2 -= 1
    print(min(num1, num2))
