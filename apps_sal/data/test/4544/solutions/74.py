input()
c = [0] * 10**6
for i in input().split():
    for j in (0, 1, 2):
        c[int(i) + j] += 1
print(max(c))
