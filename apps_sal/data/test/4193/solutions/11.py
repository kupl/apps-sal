def main():
    A = [list(map(int, input().split())) for i in range(3)]
    N = int(input())
    b = [int(input()) for _ in range(N)]
    for i in range(N):
        for j in range(3):
            for h in range(3):
                if A[j][h] == b[i]:
                    A[j][h] = 0
    if A[0][0] == 0 and A[0][1] == 0 and (A[0][2] == 0):
        return 'Yes'
    elif A[1][0] == 0 and A[1][1] == 0 and (A[1][2] == 0):
        return 'Yes'
    elif A[2][0] == 0 and A[2][1] == 0 and (A[2][2] == 0):
        return 'Yes'
    elif A[0][0] == 0 and A[1][0] == 0 and (A[2][0] == 0):
        return 'Yes'
    elif A[0][1] == 0 and A[1][1] == 0 and (A[2][1] == 0):
        return 'Yes'
    elif A[0][2] == 0 and A[1][2] == 0 and (A[2][2] == 0):
        return 'Yes'
    elif A[0][0] == 0 and A[1][1] == 0 and (A[2][2] == 0):
        return 'Yes'
    elif A[0][2] == 0 and A[1][1] == 0 and (A[2][0] == 0):
        return 'Yes'
    return 'No'


print(main())
