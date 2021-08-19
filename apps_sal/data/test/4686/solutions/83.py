from collections import Counter
w = input()
w = Counter(w)
result = 'Yes'
for v in w.values():
    if v % 2 == 0:
        continue
    else:
        result = 'No'
        break
print(result)
