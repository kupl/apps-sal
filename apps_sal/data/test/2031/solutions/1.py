import copy
n = int(input())
mins = [0] * n
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    f = a.copy()
    k, pos = list(map(int, input().split()))
    for l in range(n - k):
        if mins[l] == 0:
            mins[l] = min(f)
        for j in range(len(f) - 1, -1, -1):
            if f[j] == mins[l]:
                f.pop(j)
                break
    print(f[pos - 1])
