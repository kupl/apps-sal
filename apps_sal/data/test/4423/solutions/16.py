n = int(input())
a = sorted([input().split() + [i + 1] for i in range(n)], key=lambda x: (x[0], -int(x[1])))
for (n, s, i) in a:
    print(i)
