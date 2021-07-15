import sys
import math
import random
import time

def func_cnk(keepers, defenders, attackers, flag):
    if flag == 'kpr':
        kpr = 1
        defs = math.factorial(defenders) // math.factorial(2) // math.factorial(defenders - 2)
        atts = math.factorial(attackers) // math.factorial(3) // math.factorial(attackers - 3)
    elif flag == 'def':
        kpr = keepers
        defs = defenders - 1
        atts = math.factorial(attackers) // math.factorial(3) // math.factorial(attackers - 3)
    elif flag == 'att':
        kpr = keepers
        defs = math.factorial(defenders) // math.factorial(2) // math.factorial(defenders - 2)
        atts = math.factorial(attackers - 1) // math.factorial(2) // math.factorial(attackers - 3)
    return kpr * int(defs) * int(atts)

g, d, f = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))
#N = 100000
#x = random.sample(range(1, N), g)
#y = random.sample(range(1, N), d)
#z = random.sample(range(1, N), f)
#print(x, y, z)

if (d < 2) or (f < 3):
    print('0')
    return

t = time.time()

res_ans = 0
dict_nums = {}

for num in x:
    dict_nums[num] = 'kpr'
for num in y:
    dict_nums[num] = 'def'
for num in z:
    dict_nums[num] = 'att'

all_nums = x + y + z
all_nums.sort()

for i in range(len(all_nums)):
    upper = all_nums[i] * 2
    j = i
    keepers = 0
    defenders = 0
    attackers = 0
    while (j < len(all_nums) and (all_nums[j] <= upper)):
        if dict_nums[all_nums[j]] == 'kpr':
            keepers = keepers + 1
        if dict_nums[all_nums[j]] == 'def':
            defenders = defenders + 1
        if dict_nums[all_nums[j]] == 'att':
            attackers = attackers + 1
        j = j + 1
    if (keepers > 0) and (defenders > 1) and (attackers > 2):
        #print(all_nums[i], func_cnk(keepers, defenders, attackers, dict_nums[all_nums[i]]))
        res_ans = res_ans + func_cnk(keepers, defenders, attackers, dict_nums[all_nums[i]])

print(res_ans)
