S = input()
T = []
for i in S:
    if(i not in T):
        T.append(i)

if(len(T) == 2 and S.count(T[0]) == 2 and S.count(T[1]) == 2):
    print("Yes")
else:
    print("No")
