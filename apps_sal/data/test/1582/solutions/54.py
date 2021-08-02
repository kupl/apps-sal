N = int(input())
results = {(str(i), str(j)): 0 for i in range(1, 10) for j in range(1, 10)}


for i in range(N + 1):
    s = str(i)
    if (s[0], s[-1]) in results.keys():
        results[(s[0], s[-1])] += 1

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        cnt += results[(str(i), str(j))] * results[(str(j), str(i))]

print(cnt)
