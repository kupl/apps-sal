n, x, m = list(map(int, input().split()))
X = [-1] * m
P = []
sum_p = 0
while X[x] == -1:  # preset
    X[x] = len(P)  # pre length
    P.append(sum_p)  # pre sum_p
    sum_p += x  # now sum_p
    x = x * x % m
P.append(sum_p)  # full sum_p

p_len = len(P) - 1
if n <= p_len:
    print((P[n]))  # sum_p
    return

cyc_times, nxt_len = divmod(n - X[x], p_len - X[x])
cyc = (sum_p - P[X[x]]) * cyc_times
remain = P[X[x] + nxt_len]
print((cyc + remain))
