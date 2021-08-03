N = int(input())
res = [2, 1]

for i in range(N - 1):
    res.append(res[-1] + res[-2])
print(res[-1])
