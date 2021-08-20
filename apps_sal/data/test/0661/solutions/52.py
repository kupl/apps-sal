import itertools
(M, K) = map(int, input().split())
if M == 1 and K == 1:
    print(-1)
elif K == 0:
    ans_list = []
    for i in range(2 ** M):
        ans_list.extend([i, i])
    print(*ans_list)
elif K < 2 ** M:
    ans_list = []
    for i in range(K + 1):
        ans_list.append(i)
    for i in reversed(range(K)):
        ans_list.append(i)
    for i in reversed(range(K, 2 ** M)):
        ans_list.append(i)
    for i in range(K + 1, 2 ** M):
        ans_list.append(i)
    print(*ans_list)
else:
    print(-1)
