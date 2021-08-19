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
    (X, Y) = list(map(int, input().split()))
    if X not in cnt_dict:
        cnt_dict[X] = 0
    if Y not in cnt_dict:
        cnt_dict[Y] = 0
    s -= cnt_dict[X] * X
    s += cnt_dict[X] * Y
    cnt_dict[Y] += cnt_dict[X]
    cnt_dict[X] = 0
    print(s)
'\n#初期案\u3000遅すぎ\n\nN = int(input())\nA = list(map(int,input().split()))\nQ = int(input())\n\n\n\nfor i in range(Q):\n    X,Y = map(int,input().split())\n\n    ans = 0\n\n    for j in range(N):\n        if A[j] == X:\n            ans += Y\n            A[j] = Y\n        else:\n            ans += A[j]\n\n    print(ans)\n\n    '
