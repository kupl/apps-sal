n = int(input())
a = list(map(int, input().split(" ")))
t = max(a)
k = [0] * (t + 2)
for el in a:
    k[el] += 1
if k[1]:
    k[1] = 1
for j in range(2, t + 2):
    for i in range(2 * j, t + 2, j):
        k[j] += k[i]
print(max(k))
