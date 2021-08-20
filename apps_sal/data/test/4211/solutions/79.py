N = int(input())
B_List = list(map(int, input().split()))
A_List = [[] for i in range(N)]
A_List[0] = B_List[0]
A_List[1] = B_List[0]
for i in range(1, N - 1):
    if B_List[i] <= B_List[i - 1]:
        A_List[i] = B_List[i]
    A_List[i + 1] = B_List[i]
print(sum(A_List))
