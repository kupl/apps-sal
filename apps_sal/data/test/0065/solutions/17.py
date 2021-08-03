k = int(input())
x = list(map(int, input().split()))
m = min(x)
z = []
for i in range(k):
    if x[i] == m:
        z += [i]
j = []
for i in range(1, len(z)):
    j += [z[i] - z[i - 1]]
print(min(j))
