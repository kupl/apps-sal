from collections import Counter

n = int(input())
s = input()
keys = Counter()
need = 0
for i in range(0, n*2-2, 2):
    keys[s[i]] += 1
    neededkey = s[i+1].lower()
    if keys[neededkey]:
        keys[neededkey] -= 1
    else:
        need += 1
print(need)

