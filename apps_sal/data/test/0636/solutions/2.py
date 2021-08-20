(n, k) = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(zip(data, range(1, len(data) + 1)), key=lambda x: x[0])
inst = []
for x in data:
    if k < x[0]:
        break
    inst.append(x[1])
    k -= x[0]
print(len(inst))
print(' '.join(map(str, inst)))
