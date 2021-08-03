n = int(input())
data = list(map(int, input().split()))
if data[-1] == 0:
    print("UP")
elif data[-1] == 15:
    print("DOWN")
else:
    if n == 1:
        print(-1)
    elif data[-1] - data[-2] > 0:
        print("UP")
    else:
        print("DOWN")
