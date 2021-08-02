n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
T = sum(t)
ansv = [0]
for i in range(n):
    ansv[-1] = min(ansv[-1], v[i])
    for j in range(t[i] * 2):
        ansv.append(v[i])
ansv[-1] = 0
# for i in range(len(ansv)):
#  print(i/2,ansv[i])
for i in range(2 * T):
    ansv[i + 1] = min(ansv[i] + 0.5, ansv[i + 1])
for i in range(2 * T, 0, -1):
    ansv[i - 1] = min(ansv[i] + 0.5, ansv[i - 1])
print((sum(ansv) / 2))
# print(len(ansv))
# for i in range(len(ansv)):
#  print(i/2,ansv[i])
