n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(n):
    k = input()
    if k in a:
        a.remove(k)
    else:
        b.append(k)
c = [0, 0, 0, 0]
for i in range(len(a)):
    c[len(a[i]) - 1] += 1
print(sum(c))
