Sum = sum(list(map(int, input().split())))
if Sum % 5 == 0 and Sum // 5 != 0:
    print(Sum // 5)
else:
    print(-1)
