a, b = list(map(int, input().split()))

S = input()
d = 0
c = a + b + 3
for i in range(a + b + 1):
    if S[i] == '-':
        c = i + 1
        d += 1

if c == a + 1 and d == 1:
    print('Yes')
else:
    print('No')
