import sys

input = sys.stdin.readline

n = int(input())

count = {}
for i in range(n):
    a = set(list(map(int, input().split()))[1:])
    for j in a:
        if j not in count.keys():
            count[j] = 0
        count[j] += 1

ans = []
for key in count.keys():
    if count[key] == n:
        ans.append(key)

print(" ".join([str(x) for x in ans]))
