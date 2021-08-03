N, M = list(map(int, input().split()))
num_list = list(map(int, input().split()))

x = N - sum(num_list)
if x >= 0:
    print(x)
else:
    print((-1))
