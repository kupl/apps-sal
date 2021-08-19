import numpy as np
max_num = 10 ** 5
prime_flag_l = np.ones(max_num + 1)
prime_flag_l[0] = 0
prime_flag_l[1] = 0
for i in range(1, int(np.sqrt(max_num))):
    if not prime_flag_l[i]:
        continue
    for j in range(i * 2, max_num + 1, i):
        prime_flag_l[j] = 0
like_2017_flag_l = np.zeros(max_num + 1)
for i in range(max_num + 1):
    if i % 2 == 0:
        continue
    if prime_flag_l[i] and prime_flag_l[int((i + 1) / 2)]:
        like_2017_flag_l[i] = 1
s_l = np.zeros(max_num + 1)
for i in range(max_num):
    s_l[i + 1] = s_l[i] + like_2017_flag_l[i]
Q = int(input())
for _ in range(Q):
    (l, r) = list(map(int, input().split()))
    print(int(s_l[r + 1] - s_l[l]))
