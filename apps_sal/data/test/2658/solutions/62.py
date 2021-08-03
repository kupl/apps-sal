from collections import defaultdict

N, K = map(int, input().split())
A = [int(i) for i in input().split()]
used_dict = defaultdict(int)
used_dict[0] += 1
now_town = 0
flag = False

for i in range(min(N, K)):
    now_town = A[now_town] - 1
    if used_dict[now_town]:
        used_dict[now_town] += 1
        break
    used_dict[now_town] += 1
else:
    flag = True

if not flag:
    now_town2 = 0
    cnt = 0
    while 1:
        if now_town2 == now_town:
            for _ in range((K - cnt) % (i - cnt + 1)):
                now_town = A[now_town] - 1
            break
        now_town2 = A[now_town2] - 1
        cnt += 1
print(now_town + 1)
