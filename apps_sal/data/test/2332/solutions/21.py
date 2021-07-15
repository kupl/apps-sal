from sys import stdin

all_in = stdin.read().split('\n')

n, k, m = list(map(int, all_in[0].split()))
dict_ = {s: i for i, s in enumerate(all_in[1].split(), 1)}
a = list(map(int, all_in[2].split()))
s = all_in[k + 3].split()

for i in range(3, k + 3):
    x, *set_ = list(map(int, all_in[i].split()))

    mn = min([a[j - 1] for j in set_])

    for j in set_:
        a[j - 1] = mn

print(sum([a[dict_[el] - 1] for el in s]))

