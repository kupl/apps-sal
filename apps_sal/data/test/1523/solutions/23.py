(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
i = 0
done = {}
different = 0
dif = set()
for item in a:
    if item not in dif:
        dif.add(item)
        different += 1
    if item not in done:
        done[item] = [b[i]]
    else:
        done[item].append(b[i])
    i += 1
tot = []
for item in done:
    done[item].sort()
    for i in done[item]:
        tot.append(i)
    tot.pop()
tot.sort()
counter = 0
for item in range(k - different):
    counter += tot[item]
print(counter)
