(a, b, n) = map(int, input().split())
Alist = list(range(a, min(a + n, b + 1), 1))
Blist = list(range(max(a, b - n + 1), b + 1, 1))
C = sorted(set(Alist) | set(Blist))
for i in list(C):
    print(i)
