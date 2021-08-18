n = int(input())
d = [0] * (10**5 + 1)
a = list(map(int, input().split()))
varies = len(set(a))
for v in a:
    d[v] += 1
two = 0
for i in range(len(d)):
    if d[i] > 0 and d[i] % 2 == 0:
        two += 1
print((varies if two % 2 == 0 else varies - 1))
