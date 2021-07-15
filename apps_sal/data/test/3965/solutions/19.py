vowels = ['a', 'e', 'i', 'o', 'u', 'y']

n = int(input())
p = [ int(x) for x in input().split() ]

r = True

for i in range(0, n):
    s = input()
    v = 0
    for c in vowels:
        v += s.count(c)
    if v != p[i]:
        r = False

if r:
    print('YES')
else:
    print('NO')

