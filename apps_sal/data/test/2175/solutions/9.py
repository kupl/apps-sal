import copy
n = int(input())
ocu = [0] + list(map(int, input().split()))
V = dict()
for i in range(1, n + 1):
    V[i] = ocu[i]
ocu = [0] * (n + 1)
stream = [0] * (n + 1)
l = 0
ans = []
for i in range(1, n):
    stream[i] = i + 1
stream[n] = 0
m = int(input())
for i in range(m):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x0, p = s[1], s[2]
        x = x0
        temp1 = set()
        while True:
            if p < V[x] - ocu[x]:
                ocu[x] += p
                break
            else:
                p -= V[x] - ocu[x]
                ocu[x] = V[x]
                temp1.add(x)
                x = stream[x]
                if x == 0: break
        for a in temp1:
            stream[a] = x
    if s[0] == 2:
        ans.append(ocu[s[1]])
print('\n'.join(map(str, ans)))
