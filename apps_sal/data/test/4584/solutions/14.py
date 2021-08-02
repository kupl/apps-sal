N = int(input())
dct = {}
A = list(map(int, input().split()))
for a in A:
    if a in dct.keys():
        dct[a] += 1
    else:
        dct[a] = 1
for n in range(1, N + 1):
    print(dct.get(n, 0))
