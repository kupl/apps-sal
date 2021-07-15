n = int(input())
p = list(map(int, input().split()))
antiR = [0] * n
antiR[0] -= 1
mymax = p[0]
mymin = 0
indmax = 0
indmin = -1
for i in range(1, n):
    if mymin < p[i] < mymax:
        antiR[indmax] += 1
        mymin = p[i]
        indmin = i
    elif p[i] > mymax:
        mymin, mymax, indmax, indmin = mymax, p[i], i, indmax
        antiR[i] -= 1

m = max(antiR)
mini = 10 ** 9
for i in range(n):
    if antiR[i] == m:
        mini = min(mini, p[i])
print(mini)
