N = int(input())
d = {}
for i in range(N):
    l = input()
    if l not in d:
        d[l] = 0
    d[l] += 1

print(max(d.values()))
