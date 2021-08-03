n = int(input())
d = {}

for i in range(n):
    s = input()
    if s not in d:
        d.update({s: 1})
    else:
        d[s] += 1

max_val = max(d.values())
keys_of_max_val = [key for key in d if d[key] == max_val]
print(("\n".join(sorted(keys_of_max_val))))
