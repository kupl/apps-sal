n = int(input())
a = list(sorted(map(int, input().split())))
b = list(sorted(map(int, input().split())))
s = []
ei = 0
for i in range(5):
    t = [a.count(i + 1), b.count(i + 1)]
    s.append(t[0] - t[1])
    if sum(t) % 2 == 1:
        ei = 1
if bool(ei):
    print(-1)
else:
    print(int(sum([x for x in s if x > 0]) / 2))
