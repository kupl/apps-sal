__author__ = 'Andrey'
(n, s) = list(map(int, input().split()))
B = dict()
S = dict()
for i in range(n):
    t = input().split()
    if t[0] == 'B':
        B[int(t[1])] = B.get(int(t[1]), 0) + int(t[2])
    else:
        S[int(t[1])] = S.get(int(t[1]), 0) + int(t[2])
B_keys = sorted(list(B.keys()), reverse=True)
S_keys = sorted(S.keys())
if B_keys:
    b_s = B_keys[min(s - 1, len(B_keys) - 1)]
if S_keys:
    s_s = S_keys[min(s - 1, len(S_keys) - 1)]
    for key_1 in sorted(list(S.keys()), reverse=True):
        if key_1 <= s_s:
            print('S', key_1, S[key_1])
if B_keys:
    b_s = B_keys[min(s - 1, len(B_keys) - 1)]
    for key_2 in sorted(list(B.keys()), reverse=True):
        if key_2 >= b_s:
            print('B', key_2, B[key_2])
