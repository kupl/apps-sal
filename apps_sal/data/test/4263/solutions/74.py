X = str(input())
N = len(X)
ans = 0
count = 0
for i in range(N):
    if X[i] == "A" or X[i] == "C" or X[i] == "G" or X[i] == "T":
        count += 1
    else:
        ans = max(ans, count)
        count = 0
else:
    ans = max(ans, count)
print(ans)
