n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(n):
    l.append([a[i], i + 1])
l = sorted(l)
ans = []
for j in range(n):
    ans.append(str(l[j][1]))
print(" ".join(ans))
