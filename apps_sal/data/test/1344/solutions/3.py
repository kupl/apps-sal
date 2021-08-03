n = int(input())
l = input().split()
best = 1
curr = 1
for i in range(n - 1):
    if int(l[i]) < int(l[i + 1]):
        curr += 1
    else:
        curr = 1
    best = max(best, curr)
print(best)
