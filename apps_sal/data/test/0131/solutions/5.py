n = int(input())
data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
if sum(data_1) >= sum(data_2):
    print('Yes')
else:
    print('No')
