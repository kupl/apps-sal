from collections import Counter
(N, *A) = map(int, open(0).read().split())
ac = Counter(A)
e = [x[0] for x in ac.items() if x[1] % 2 == 0]
if len(e) % 2 == 0:
    print(len(ac))
else:
    print(len(ac) - 1)
