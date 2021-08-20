import itertools as it
N = int(input())
L = list(map(int, input().split()))
c = it.combinations(L, 3)
count = 0
for i in c:
    if len(set(i)) == 3:
        (a, b, c) = sorted(i, reverse=True)
        if a < b + c:
            count += 1
print(count)
