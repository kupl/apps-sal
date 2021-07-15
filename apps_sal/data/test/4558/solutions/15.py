def LI():
    return list(map(int, input().split()))


X, t = LI()
ans = max(X-t, 0)
print(ans)

