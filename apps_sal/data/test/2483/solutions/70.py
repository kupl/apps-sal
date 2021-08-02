A, B = list(map(int, input().split()))
l = [[] for i in range(100001)]
for i in range(A):
    X, Y, Z = list(map(int, input().split()))
    for j in range(X - 1, Y):
        l[j].append(Z)
ans = 0
for i in l:
    ans = max(ans, len(set(i)))
print(ans)
