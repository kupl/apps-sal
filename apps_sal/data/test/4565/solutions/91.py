N = int(input())
N_List = str(input())
C_Ans = N_List[1:].count("E")
Ans = C_Ans
for i in range(1, N):
    C_Ans = C_Ans + (0, 1)[N_List[i - 1] == "W"] - (0, 1)[N_List[i] == "E"]
    if C_Ans < Ans:
        Ans = C_Ans

print(Ans)
