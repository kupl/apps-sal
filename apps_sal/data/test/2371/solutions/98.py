N, Z, W = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    print(abs(W - A[0]))
else:
    # Xが自由に決定できるのは結局A[-1] - WかA[-1] - A[-2]の二通りのみ
    # 2枚以上カードを残してもYによってA[-1] - A[-2]にされてしまう
    # いくら他に値が大きくなる手があっても結局この二手に限られてしまうので
    # その中の最大値を出力する
    ans = max(abs(A[-1] - W), abs(A[-1] - A[-2]))
    print(ans)
