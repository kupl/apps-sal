n = int(input())
A = []
bool = [True] * n
for i in range(n):
    a = int(input())
    a -= 1
    A.append(a)
j = A[0]
cnt = 1
for i in range(n):
    if j == 1:
        print(cnt)
        return
    if bool[A[j]] == True:
        bool[A[j]] = False        
        j = A[j]
        cnt += 1
    else :
        print((-1))
        return



