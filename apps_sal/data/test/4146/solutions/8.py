N = int(input())
V = list(map(int, input().split()))
O = []
E = []
nums_O = []
nums_E = []
for i in range(0, N, 2):
    O.append(V[i])
    E.append(V[i + 1])
for j in range(100000):
    nums_O.append([0, j])
    nums_E.append([0, j])
for k in range(N // 2):
    nums_O[O[k] - 1][0] += 1
    nums_E[E[k] - 1][0] += 1
nums_O.sort()
nums_E.sort()
if nums_O[-1][1] != nums_E[-1][1]:
    print(N - (nums_O[-1][0] + nums_E[-1][0]))
else:
    print(N - max(nums_E[-2][0] + nums_O[-1][0], nums_O[-2][0] + nums_E[-1][0]))
