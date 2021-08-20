N = int(input())
d = []
for i in range(N):
    d.append(int(input()))
d.sort(reverse=True)
step = 1
for i in range(N - 1):
    if d[i] > d[i + 1]:
        step += 1
print(step)
