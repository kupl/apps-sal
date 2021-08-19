N = int(input())
S = input()
T = list((1 if c == '(' else -1 for c in S))
(l, l_min) = (0, 0)
(r, r_min) = (0, 0)
for i in range(N):
    l += T[i]
    l_min = min(l_min, l)
    r -= T[N - i - 1]
    r_min = min(r_min, r)
print(''.join(['(' * -l_min, S, ')' * -r_min]))
