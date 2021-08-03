li = list(map(int, input().split()))
D = li[0]
T = li[1]
S = li[2]
if S * T >= D:
    print("Yes")
else:
    print("No")
