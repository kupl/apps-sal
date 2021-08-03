h1, a1, c1 = map(int, input().split())
h2, a2 = map(int, input().split())
k = 0
if h2 % a1 == 0:
    n = h2 // a1 - 1
else:
    n = h2 // a1
while k <= (n * a2 - h1) / (c1 - a2):
    k += 1
print(k + n + 1)
for i in range(k):
    print('HEAL')
for i in range(n + 1):
    print('STRIKE')
