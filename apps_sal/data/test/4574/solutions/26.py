with open(0) as f:
    N, *A = map(int, f.read().split())

pair = []
unpair = set()
for a in A:
    if a in unpair:
        unpair.remove(a)
        pair.append(a)
    else:
        unpair.add(a)
pair.sort()
print(pair.pop()*pair.pop() if len(pair) > 1 else 0)
