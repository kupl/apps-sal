n = int(input())
D = []
for _ in range(n):
    d = int(input())
    D += [d]
print(len(set(D)))
