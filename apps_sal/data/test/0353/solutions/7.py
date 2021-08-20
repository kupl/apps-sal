n = int(input())
A = list(map(int, input().split()))
if n == 1:
    if A[0] == 15:
        print('DOWN')
    elif A[0] == 0:
        print('UP')
    else:
        print(-1)
else:
    per = A[-1]
    per2 = A[-2]
    if per == 15:
        print('DOWN')
    elif per == 0:
        print('UP')
    elif per > per2:
        print('UP')
    else:
        print('DOWN')
