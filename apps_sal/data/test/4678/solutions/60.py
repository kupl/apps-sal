n = int(input())
l = list(map(int, input().split()))
al = []
for i in range(0, n - 1):
    if l[i] <= l[i + 1]:
        al.append(0)
    else:
        al.append(l[i] - l[i + 1])
        l[i + 1] = l[i]
print(sum(al))
