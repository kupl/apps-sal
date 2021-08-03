import itertools
n, k = map(int, input().split())
d = list(map(int, input().split()))
safe = [i for i in range(10) if i not in d]

n_l = list(map(int, list(str(n))))
if len(set(safe) & set(n_l)) == len(set(n_l)):
    print(n)
    return

for v in itertools.product(safe, repeat=len(str(n))):
    if v[0] == 0:
        continue
    x = int("".join(list(map(str, v))))
    if int(x) >= n:
        print(x)
        return

for v in itertools.product(safe, repeat=len(str(n)) + 1):
    if v[0] == 0:
        continue
    x = int("".join(list(map(str, v))))
    if int(x) >= n:
        print(x)
        return
