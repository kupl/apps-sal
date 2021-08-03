import bisect
n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
vc = [0] * n
for i in range(n):
    vc[i] = v[i] - c[i]
vc2 = sorted(vc)
print(sum(vc2[bisect.bisect_left(vc2, 0):]))
