(N, M) = list(map(int, input().split()))
A_list = []
for i in range(1, M + 1):
    A_list.append('A_' + str(i))
A_list = list(map(int, input().split()))
answer = N - sum(A_list)
if answer >= 0:
    print(answer)
else:
    print(-1)
