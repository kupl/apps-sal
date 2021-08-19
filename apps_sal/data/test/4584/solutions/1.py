import collections
n = int(input())
li = list(map(int, input().split()))
res = [0] * (n + 1)
for i in li:
    res[i] += 1
for i in range(1, len(res)):
    print(res[i])
