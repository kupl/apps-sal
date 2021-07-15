from collections import defaultdict
import string
s = input()
K = int(input())
location = defaultdict(list)
for i, s_i in enumerate(s):
    location[s_i].append(i)
count = 0
s_list = []
for c in string.ascii_lowercase[:26]:
    if location[c] == []:
        continue
    for idx in location[c]:
        for i in range(K):
            if idx + i + 1 > len(s):
                break
            if s[idx:idx+i+1] in s_list:
                continue
            s_list.append(s[idx:idx+i+1])
    count += 1
    if count == K:
        break
s_list.sort()
print(s_list[K-1])
