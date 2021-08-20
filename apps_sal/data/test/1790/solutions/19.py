n = int(input())
R = [list(map(int, input().split())) for i in range(n)]
SET = set(R[0][1:])
for i in range(1, n):
    SET = SET & set(R[i][1:])
for s in SET:
    print(s, end=' ')
