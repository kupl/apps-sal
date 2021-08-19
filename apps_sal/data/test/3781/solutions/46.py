import collections
I = [int(_) for _ in open(0).read().split()]
T = I[0]
i = 1
N = []
A = []
for _ in range(T):
    N += [I[i]]
    i += 1
    A += [I[i:i + N[-1]]]
    i += N[-1]
for (n, a) in zip(N, A):
    if n % 2 == 0 and any((v % 2 for v in list(collections.Counter(a).values()))):
        print('First')
    else:
        print('Second')
