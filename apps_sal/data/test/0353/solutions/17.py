
n = int(input())
days = list(map(int, input().split()))

if days[-1] == 0:
    print("UP")
elif days[-1] == 15:
    print("DOWN")
elif n == 1:
    print("-1")
else:
    if days[-1] - days[-2] > 0:
        print("UP")
    else:
        print("DOWN")
