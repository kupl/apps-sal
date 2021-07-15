3

import sys
import itertools

#Approach: Since there are only 5 students, we can brute force through all 5! (=120) lineups. Don't know if that will be fast enough, though, but let's see. We'll go through each lineup, and measure the happiness.

h_1 = list(map(int, input().split())) #i's happiness
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
	hap = hap + all_hap[perm[0]][perm[1]] + all_hap[perm[1]][perm[0]] + all_hap[perm[2]][perm[3]] + all_hap[perm[3]][perm[2]]#When no one is showering.
	hap = hap + all_hap[perm[1]][perm[2]] + all_hap[perm[2]][perm[1]] + all_hap[perm[3]][perm[4]] + all_hap[perm[4]][perm[3]]#When first guy is in the shower
	hap = hap + all_hap[perm[2]][perm[3]] + all_hap[perm[3]][perm[2]]#When second guy is in the shower
	hap = hap +all_hap[perm[3]][perm[4]] + all_hap[perm[4]][perm[3]]#When third guy is in the shower
	if (hap > max_hap):
		max_hap = hap

print(max_hap)

