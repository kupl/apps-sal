N,_,W = map(int, input().split())
A = [int(i) for i in input().split()]

if N == 1:
    ans = abs(A[0] - W)
else:
    # 1枚残す場合
    ans = abs(A[-1] - A[-2])
    # 0枚残す場合
    ans = max(ans, abs(A[-1] - W))

print(ans)
