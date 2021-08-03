def calc(T, x):
    return T - x * 0.006


N = int(input())
T, A = map(int, input().split())
L = list(map(int, input().split()))
l = []
for i in L:
    l.append(abs(A - calc(T, i)))

mi = min(l)
print(l.index(mi) + 1)
