n = int(input())
a = list(map(int, input().split()))
mn = min(a)
incs = []
for i in range(len(a)):
    if a[i] == mn:
        incs.append(i)
print(min([incs[i] - incs[i - 1] for i in range(1, len(incs))]))
