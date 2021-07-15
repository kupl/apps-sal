n = int(input())
list_a = []
for i in range(n):
    list_a.append(int(input()))

from collections import Counter

counter = dict(Counter(list_a))
sorted_counter = sorted(counter, reverse=True)

for item in list_a:
    counter[item] -= 1
    for submax in sorted_counter:
        if counter[submax] == 0:
            continue
        print(submax)
        break
    counter[item] += 1
