n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
nl = []
for i in range(len(v)):
    if v[i] - c[i] > 0:
        nl.append(v[i] - c[i])
nl.sort(reverse=True)
print(sum(nl[:n]))
