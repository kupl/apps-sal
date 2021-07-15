n, k = map(int, input().split())
list_X = list(map(int, input().split()))
ans = pow(10, 14)

for i in range(n - k + 1):
    if list_X[i] * list_X[i + k - 1] < 0:
        ans = min(ans, list_X[i + k - 1] - list_X[i] + min(abs(list_X[i]), abs(list_X[i + k - 1])))
    else:
        ans = min(ans, max(abs(list_X[i + k - 1]), abs(list_X[i])))

print(ans)
