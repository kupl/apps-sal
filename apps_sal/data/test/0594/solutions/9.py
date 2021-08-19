(m, n) = map(int, input().split())
(trues, falses) = (list(map(int, input().split())), list(map(int, input().split())))
v = max(2 * min(trues), max(trues))
if v < min(falses):
    print(v)
else:
    print(-1)
