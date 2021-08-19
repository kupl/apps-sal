N = int(input())
A = [int(input()) for _ in range(N)]
d = {}
for i in A:
    d[i] = 0
for i in A:
    if d[i] == 1:
        d[i] = 0
    else:
        d[i] = 1
print(sum(d.values()))
