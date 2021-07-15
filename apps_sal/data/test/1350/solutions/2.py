n, k = map(int, input().split(' '))
s = input()
m = 10 ** 10
for i in range(k):
    c = chr(ord('A') + i)
    m = min(m, s.count(c))
print(m * k)
