from collections import Counter
n = int(input())
sequence = list(map(int, input().split()))
numset = list(set(sequence))
k = len(numset)
numset.sort()
cnt = Counter(sequence)
f = [0] * (k + 1)
f[1] = cnt[numset[0]] * numset[0]
f[0] = 0
for i in range(2, k + 1):
    if numset[i - 1] - numset[i - 2] == 1:
        f[i] = max(f[i - 1], f[i - 2] + cnt[numset[i - 1]] * numset[i - 1])
    else:
        f[i] = numset[i - 1] * cnt[numset[i - 1]] + f[i - 1]
print(f[k])
'\nimport timeit\n\ns = """\nk = list(set(a))\ncnt = Counter(a)\nprint cnt\n"""\n\nsetup = """\nfrom random import randint\nn = 100000\na = [randint(1,n) for i in range(n)]\nfrom collections import Counter\n\n"""\n\n\nprint(timeit.timeit(stmt=s, number=1, setup=setup))\n'
