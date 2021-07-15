
H, N = map(int, input().split())
A_list = []
for i in range(1, N+1):
    A_list.append("A_" + str(i))

A_list = map(int, input().split())
A_total = sum(A_list)

if A_total >= H:
    print("Yes")
else:
    print("No")
