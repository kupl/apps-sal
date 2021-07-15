p = input()
n, t = len(p), [len(i) + 6 for i in p.split('bear')]
t[0] -= 3
t[-1] -= 3
print(3 * (len(t) - 1) + (n * (n + 1) - sum(i * (i + 1) for i in t)) // 2)
