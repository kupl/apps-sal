n = int(input())

t = []
m = 1
while 3 ** m <= 10 ** 18:
    t.append(3 ** m)
    m += 1

f = []
m = 1
while 5 ** m <= 10 ** 18:
    f.append(5 ** m)
    m += 1

for a, i in enumerate(t):
    for b, j in enumerate(f):
        if i + j == n:
            print(a + 1, b + 1)
            return
print(-1)
