A = str(input())
P = str(input())
cnt = 0
for i in range(3):
    if A[i] == P[i]:
        cnt += 1
print(cnt)
