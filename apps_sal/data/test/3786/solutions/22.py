inflos = int(input())
roots = input()
roots = [int(x) - 1 for x in roots.split()]
 

son = [0]
for v in range(inflos - 1):
    son.append(son[roots[v]] + 1)

freq = {}

for d in son:
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1
res = 0
for d in freq:
    res+= freq[d]%2
print(res)
