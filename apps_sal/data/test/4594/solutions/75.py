N = int(input())
D = []
for i in range(N):
    D.append(int(input()))

count = 0
preMax = 0
for i in range(N):
    if len(D) == 0:
        break
    if preMax != max(D):
        count += 1
        preMax = max(D)
    D.remove(max(D))

print(count)
