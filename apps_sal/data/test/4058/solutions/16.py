(n, r) = list(map(int, input().split()))
mas = list(map(int, input().split()))
masn = [0 for i in range(n)]
for i in range(n):
    if mas[i] == 1:
        for j in range(max(0, i - r + 1), min(n, i + r)):
            masn[j] = i + 1
ind = 0
otv = 0
br = False
while ind < n:
    if masn[ind] > 0:
        otv += 1
        ind = masn[ind] - 1 + r
    else:
        br = True
        break
if br:
    print(-1)
else:
    print(otv)
