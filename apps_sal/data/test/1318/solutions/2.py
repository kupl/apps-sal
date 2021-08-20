n = int(input())
P = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    P.append((y, x, i))
k = int(input())
L = list(map(int, input().split()))
for i in range(k):
    L[i] = (L[i], i)
L.sort()
P.sort(reverse=True)
ans = 0
Taken = [False] * k
r = 0
Ans = [-1] * n
for i in range(n):
    for j in range(k):
        if L[j][0] >= P[i][1] and Taken[j] == False:
            Taken[j] = True
            ans += P[i][0]
            r += 1
            Ans[P[i][2]] = L[j][1]
            break
print(r, ans)
for i in range(n):
    if Ans[i] == -1:
        continue
    print(i + 1, Ans[i] + 1)
