N = int(input())
A = [int(x) for x in input().split()]

data = {}
for a in A:
    for i in range(3):
        if a - 1 + i in data:
            data[a - 1 + i] += 1
        else:
            data[a - 1 + i] = 1

ans = 0
for d in data.values():
    ans = max(ans, d)
print(ans)
