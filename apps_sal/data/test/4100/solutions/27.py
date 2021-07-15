N, K, Q = list(map(int, input().split()))

ans_cnt_list = [K-Q]*N
for i in range(Q):
    A = int(input())
    ans_cnt_list[A-1] += 1

for i in range(N):
    if ans_cnt_list[i] > 0:
        print('Yes')
    else:
        print('No')

