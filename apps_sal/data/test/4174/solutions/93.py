n, x = map(int, input().split())
l = list(map(int, input().split()))
wa = 0
d = [0] * (n + 3)
d[1] = 0
d.pop(0)
wa = 1
for i in range(2, n + 2):
    d[i] = d[i - 1] + l[i - 2]
    if(d[i] > x):
        break
    wa += 1
print(wa)
