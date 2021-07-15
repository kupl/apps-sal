N = int(input())
l0 = [[int(i) for i in input().split()] for _ in range(N)]
l1 = [0] * N
l2 = [0] * N
for cnt, val in enumerate(l0):
    l1[cnt] = val[0] + val[1]
    l2[cnt] = val[0] - val[1]
l1.sort()
l2.sort()
print((max(l1[-1] - l1[0], l2[-1] - l2[0])))

