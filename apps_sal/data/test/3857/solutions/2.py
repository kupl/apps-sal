n = input()
h = [0]
A = sorted(map(int, input().split()))
for x in A:
    if x < min(h):
        h += [1]
    else:
        h[h.index(min(h))] += 1
print(len(h))
