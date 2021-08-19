(X, Y, A, B, C) = map(int, input().split())
p_l = sorted(map(int, input().split()), reverse=True)
q_l = sorted(map(int, input().split()), reverse=True)
r_l = sorted(map(int, input().split()), reverse=True)
p = X
q = Y
r = 0
for i in range(min(X + Y, C)):
    if p == 0 and q == 0:
        break
    elif p == 0 and r_l[i] <= q_l[q - 1]:
        break
    elif q == 0 and r_l[i] <= p_l[p - 1]:
        break
    elif p == 0 and r_l[i] > q_l[q - 1]:
        (r, q) = (r + 1, q - 1)
    elif q == 0 and r_l[i] > p_l[p - 1]:
        (r, p) = (r + 1, p - 1)
    elif r_l[i] > q_l[q - 1] and p_l[p - 1] >= q_l[q - 1]:
        (r, q) = (r + 1, q - 1)
    elif r_l[i] > p_l[p - 1] and q_l[q - 1] >= p_l[p - 1]:
        (r, p) = (r + 1, p - 1)
    else:
        break
print(sum(p_l[:p]) + sum(q_l[:q]) + sum(r_l[:r]))
