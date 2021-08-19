k = []
(a, b) = list(map(int, input().split(' ')))
for i in range(a):
    (x, y) = list(map(int, input().split(' ')))
    k.append([x, y])
k.append([0, -1])
k.sort()
k.reverse()
curr = b
t = 0
for i in k:
    d = curr - i[0]
    curr = i[0]
    t = max(i[1], t + d)
print(t)
