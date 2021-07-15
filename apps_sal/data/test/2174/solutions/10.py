nums = int(input())
perm = list(map(int, input().split(' ')))
perm.sort()
total = 0
for i in range(len(perm)):
    total += abs(perm[i] - (i+1))
print(total)

