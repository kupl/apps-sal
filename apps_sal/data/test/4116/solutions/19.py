ls = []
for i in range(9):
    for j in range(9):
        ls.append(int((i+1) * (j+1)))
N = int(input())
if N in ls:
    print("Yes")
else:
    print("No")
