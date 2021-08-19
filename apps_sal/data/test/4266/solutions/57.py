(K, X) = map(int, input().split())
ans = []
for i in range(K):
    if i == 0:
        ans.append(X)
    else:
        ans.append(X - i)
        ans.append(X + i)
ans = sorted(ans)
ans = [str(x) for x in ans]
print(' '.join(ans))
