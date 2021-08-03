N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
sortX = sorted(X)
diffX = [sortX[i] - sortX[i - 1] for i in range(1, M)]
sdiffX = sorted(diffX)
if N == 1:
    print((sum(sdiffX)))
    return
ans = sum(sdiffX[:-(N - 1)])
print(ans)
