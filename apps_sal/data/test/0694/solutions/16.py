s = input()
a, b = map(int, input().split())
n, m = len(s), 0
I, J = set(), set()

for i in range(n - 1):
    m = (10 * m + int(s[i])) % a
    if m == 0:
        I.add(i + 1)

m, k = 0, 1

for i in range(1, n)[::-1]:
    m, k = (m + k * int(s[i])) % b, (10 * k) % b
    if m == 0:
        J.add(i)

for i in I & J:
    if s[i] != '0':
        print('YES', s[:i], s[i:], sep='\n')
        break
else:
    print('NO')
