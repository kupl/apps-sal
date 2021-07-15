import string
from collections import defaultdict

scores = [int(x) for x in input().split()]
score_dict = {letter: scores[idx] for idx, letter in enumerate(string.ascii_lowercase)}

s = input()


partial_sums = [0]
encounters = {letter: [] for idx, letter in enumerate(string.ascii_lowercase)}

for idx, c in enumerate(s):
    partial_sums.append(partial_sums[-1] + score_dict[c])
    encounters[c].append(idx)
    
partial_sums = partial_sums[1:]

count = 0

for letter in encounters:
    
    score_count_dict = defaultdict(int)
    
    for letter_idx in encounters[letter]:

        count += score_count_dict[partial_sums[letter_idx - 1]]
        score_count_dict[partial_sums[letter_idx]] += 1

        
print(count)
            
    
    
    
# partial_sums = [0]
# 
# for c in s:
#     partial_sums.append(partial_sums[-1] + score_dict[c])
#     
# partial_sums = partial_sums[1:]
# 
# encounters = {letter: [] for idx, letter in enumerate(string.ascii_lowercase)}
# 
# count = 0
# 
# for idx, c in enumerate(s):
#     
#     for evt_idx in encounters[c]:
#         score = partial_sums[idx] - partial_sums[evt_idx] - score_dict[c]
#         if score == 0:
#             count += 1
#             
#     encounters[c].append(idx)
    
# print(count)
    

