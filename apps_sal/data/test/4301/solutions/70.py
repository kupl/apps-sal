N = int(input())
lsA = [int(input()) for i in range(N)]
maxA = max(lsA)
Akazu = lsA.count(maxA)
for i in range(N):
    if lsA[i] == maxA and Akazu == 1:
        print(max(lsA[:i]+lsA[i+1:]))
    else:
        print(maxA)
