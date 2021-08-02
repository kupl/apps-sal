N, M = list(map(int, input().split()))
A_list = list(map(int, input().split()))
A_list.sort(reverse=True)

check_num = A_list[M - 1]
if check_num / sum(A_list) >= 1 / (4 * M):
    print('Yes')
else:
    print('No')
