a = int(input())
a = list(map(int, input().split()))
t = 1
maxt = 0
for i in range(1, len(a)):
    if a[i] >= a[i - 1]:
        t += 1
    else:
        maxt = max(t, maxt)
        t = 1
maxt = max(maxt, t)
print(maxt)
