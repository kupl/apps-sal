N = int(input())
A_List = list(map(int, input().split()))
B_List = list(map(int, input().split()))
C_List = list(map(int, input().split()))
ans = 0
for i in range(len(A_List)):
    ans += B_List[A_List[i] - 1]
    if (i != 0) & (A_List[i] - A_List[i - 1] == 1):
        ans += C_List[A_List[i - 1] - 1]
print(ans)
