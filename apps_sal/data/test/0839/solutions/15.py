import itertools
import sys
3


h_1 = list(map(int, input().split()))
h_2 = list(map(int, input().split()))
h_3 = list(map(int, input().split()))
h_4 = list(map(int, input().split()))
h_5 = list(map(int, input().split()))

all_hap = []
all_hap.append(h_1)
all_hap.append(h_2)
all_hap.append(h_3)
all_hap.append(h_4)
all_hap.append(h_5)

all_permutations = list(itertools.permutations([0, 1, 2, 3, 4], 5))
max_hap = 0

for perm in all_permutations:
    hap = 0
    hap = hap + all_hap[perm[0]][perm[1]] + all_hap[perm[1]][perm[0]] + all_hap[perm[2]][perm[3]] + all_hap[perm[3]][perm[2]]
    hap = hap + all_hap[perm[1]][perm[2]] + all_hap[perm[2]][perm[1]] + all_hap[perm[3]][perm[4]] + all_hap[perm[4]][perm[3]]
    hap = hap + all_hap[perm[2]][perm[3]] + all_hap[perm[3]][perm[2]]
    hap = hap + all_hap[perm[3]][perm[4]] + all_hap[perm[4]][perm[3]]
    if (hap > max_hap):
        max_hap = hap

print(max_hap)
