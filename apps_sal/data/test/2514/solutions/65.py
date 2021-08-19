N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cnt_dict = {}


s = sum(A)

ans = 0

for item in A:
    if item not in cnt_dict:
        cnt_dict[item] = 0
    cnt_dict[item] += 1

for _ in range(Q):
    X, Y = list(map(int, input().split()))

    if X not in cnt_dict:
        cnt_dict[X] = 0
    if Y not in cnt_dict:
        cnt_dict[Y] = 0

    s -= cnt_dict[X] * X
    s += cnt_dict[X] * Y

    cnt_dict[Y] += cnt_dict[X]
    cnt_dict[X] = 0

    print(s)


'''
#初期案　遅すぎ

N = int(input())
A = list(map(int,input().split()))
Q = int(input())



for i in range(Q):
    X,Y = map(int,input().split())

    ans = 0

    for j in range(N):
        if A[j] == X:
            ans += Y
            A[j] = Y
        else:
            ans += A[j]

    print(ans)

    '''
