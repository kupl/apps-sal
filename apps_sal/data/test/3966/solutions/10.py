input()
t = list(map(int, input().split()))
t.sort()
print(sum((i * x for (i, x) in enumerate(t, 2))) - t[-1])
