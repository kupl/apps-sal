A1 = 0
B1, B2, B3 = map(int, input().split())
C1, C2, C3 = map(int, input().split())
D1, D2, D3 = map(int, input().split())
flag = 0
if not(C2 - B2 == C1 - B1 and C3 - B3 == C1 - B1 and C2 - B2 == C3 - B3):
    flag = 1
if not(D2 - B2 == D1 - B1 and D3 - B3 == D1 - B1 and D2 - B2 == D3 - B3):
    flag = 1
print("Yes" if flag == 0 else "No")
