n, m = list(map(int, input().split()))

dic = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    dic[(a, b)] = True
    dic[(b, a)] = True
ans = 'IMPOSSIBLE'
for i in range(2, n):
    if dic.get((1, i), False):
        if dic.get((i, n), False):
            ans = 'POSSIBLE'
            break
print(ans)
