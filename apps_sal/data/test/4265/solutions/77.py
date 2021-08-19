s = [i for i in input()]
t = [j for j in input()]
count = 0
for (k, l) in zip(s, t):
    if k != l:
        count += 1
print(count)
