inputs = [int(x) for x in input().split()]
 
desired_weight = inputs[0]
k = inputs[1]
min_weight = inputs[2]

# desired_weight = 38
# k = 16
# min_weight = 15
# 

# desired_weight = 3
# k = 3
# min_weight = 3

saved = [{True: None, False: None} for i in range(desired_weight + 1)]
saved[desired_weight] = {True: 0, False: 0}

modulo = 1000000007

for i in reversed(range(0, desired_weight)):
#     print('*** ' + str(i) + ' ***')
    range_to_work_with = i + k
    hit_min_value = 0
    fail_to_hit_min_value = 0

    
    travel_range = range(i + 1, i + k + 1 if i + k + 1 <= desired_weight + 1 else desired_weight + 1)
#     print(travel_range)
    for j in travel_range:
        if j - i >= min_weight:
            fail_to_hit_min_value += saved[j][True]
        else:
            fail_to_hit_min_value += saved[j][False]
    fail_to_hit_min_value += 1 if desired_weight - i <= k and desired_weight - i >= min_weight else 0
            
    for j in travel_range:
        hit_min_value += saved[j][True]
    hit_min_value += 1 if desired_weight - i <= k else 0
    
    saved[i][True] = hit_min_value
    saved[i][False] = fail_to_hit_min_value
            

# print(saved)     
print(saved[0][False] % modulo)
