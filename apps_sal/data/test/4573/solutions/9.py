N = int(input())
N_List = list(map(int, input().split()))
N_List_Sorted = sorted(N_List)
B = N_List_Sorted[N // 2]
A = N_List_Sorted[N // 2 - 1]
if A == B:
    for i in range(N):
        print(A)
else:
    for i in range(N):
        if N_List[i] <= A:
            print(B)
        else:
            print(A)
