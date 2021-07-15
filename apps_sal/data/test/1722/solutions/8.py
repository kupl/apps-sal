n = int(input())
a = []
for _ in range(n):
    a.append(input()[0])
q = 0
def f(x):
    return x * (x - 1) // 2

for i in set(a):
    r = a.count(i)
    if r % 2 == 0:
        q += 2 * f(r // 2)
    else:
        q += f(r // 2) + f(r // 2 + 1)
print(q)

