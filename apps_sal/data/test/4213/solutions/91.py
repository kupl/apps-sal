N = int(input())
l = [int(i) for i in input().split()]
m = []
for i in range(N):
    for j in range(i):
        m.append(abs(l[i] - l[j]))
print(max(m))
