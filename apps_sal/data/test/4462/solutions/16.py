N = int(input())
N_List = list(map(int, input().split()))
Four_List = [i for i in N_List if i % 4 == 0]
Two_List = [i for i in N_List if i % 2 == 0]
if len(Two_List) - len(Four_List) > 0:
    N = N - (len(Two_List) - len(Four_List)) + 1
if N // 2 <= len(Four_List):
    print('Yes')
else:
    print('No')
