n = int(input())
d = list(map(int, input().split()))
d.sort(reverse=True)
x = d[0]
x_yakusuu = []
for i in range(1, 10001):
    if x % i == 0:
        x_yakusuu.append(i)
for i in x_yakusuu:
    d.remove(i)
d.sort(reverse=True)
print(str(x) + " " + str(d[0]))
