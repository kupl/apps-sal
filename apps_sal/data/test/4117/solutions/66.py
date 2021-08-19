import itertools
N = int(input())
L = list(map(int, input().split()))
count = 0
pair_list = []
for pair in itertools.combinations(L, 3):
    a = sorted(list(pair))
    if (a[0] != a[1] and a[0] != a[2] and (a[1] != a[2])) and abs(a[0] - a[1]) < a[2] and (a[2] < a[0] + a[1]):
        count = count + 1
        pair_list.append(a)
print(count)
