n = int(input())
v1 = list(map(int, input().split()))
v2 = sorted(v1)
v1, v2 = [0] + v1, [0] + v2
for i in range(1, n + 1):
    v2[i] += v2[i - 1]
    v1[i] += v1[i - 1]
m = int(input())
for i in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(v1[r] - v1[l - 1])
    else:
        print(v2[r] - v2[l - 1])
