k, n = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]
sb = set(b)
sm = [0] * k
for i in range(k):
    sm[i] = sm[i - 1] + a[i]

answers = set()
for i in range(k):
    beg = b[0] - sm[i]
    t = set([beg + sm[j] for j in range(k)])
    if len(sb - t) == 0:
        answers.add(beg)

print(len(answers))

