(x, y, a, b, c) = map(int, input().split())
p_array = list(map(int, input().split()))
q_array = list(map(int, input().split()))
r_array = list(map(int, input().split()))
p_array_sort = sorted(p_array, reverse=True)
q_array_sort = sorted(q_array, reverse=True)
r_array_sort = sorted(r_array, reverse=True)
p_i = x - 1
q_i = y - 1
for r in r_array_sort:
    p = p_array_sort[p_i]
    q = q_array_sort[q_i]
    if r <= p and r <= q:
        break
    elif q <= p:
        q_array_sort[q_i] = r
        q_i = max(q_i - 1, 0)
    else:
        p_array_sort[p_i] = r
        p_i = max(p_i - 1, 0)
ans = sum(p_array_sort[:x]) + sum(q_array_sort[:y])
print(ans)
