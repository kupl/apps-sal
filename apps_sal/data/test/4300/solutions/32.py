n = int(input())
d = list(map(int, input().split()))
d2 = d[:]
total = 0
for i in range(len(d)):
    for j in range(i, len(d2)):
        if i != j:
            total += d[i] * d[j]
print(total)
