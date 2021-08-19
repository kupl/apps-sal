y = []
a = int(input())
x = list(map(int, input().split()))
for i in x:
    y.append(bin(i).count('1'))
y.sort()
t = 0
if a == 1:
    print(0)
else:
    streak = 1
    for i in range(1, a):
        if y[i] == y[i - 1]:
            streak += 1
        else:
            t += streak * (streak - 1) / 2
            streak = 1
    t += streak * (streak - 1) / 2
    print(int(t))
