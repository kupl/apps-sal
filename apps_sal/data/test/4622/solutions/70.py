n = int(input())
S = list(map(int, input().split()))
S_set = set(S)
if len(S) == len(S_set):
    print('YES')
else:
    print('NO')
