n = int(input())
l = [int(s) for s in input().split()]
l.sort(key=int)

count = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for t in range(j + 1, len(l)):
            if l[i] + l[j] > l[t] and l[i] != l[j] != l[t]:
                count += 1
print(count)
