n, m, k = list(map(int, input().split()))
l = list(map(int, input().split()))
t = 0

for i in range(n):
    for item in map(int, input().split()):
        t += l.index(item) + 1
        l.remove(item)
        l.insert(0, item)
print(t)
