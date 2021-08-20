a = [[], []]
_ = ([[a[i].append(int(x)) for (i, x) in enumerate(input().split())] for _ in range(int(input()))], [x.sort() for x in a], print(len(a[0]) + sum((max(x, y) for (x, y) in zip(*a)))))
