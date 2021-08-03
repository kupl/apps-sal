# ABC110
# B 1 Dimensional World's Tale
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x = sorted(x, reverse=True)
y = sorted(y)
ANS = []
ans = x[0] + 1
while True:
    if ans <= y[0]:
        ANS.append(ans)
        ans = ans + 1
    else:
        break
for i in ANS:
    if X < i:
        if i < Y:
            print("No War")
            return
print("War")
