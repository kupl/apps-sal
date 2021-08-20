(x, y, a, b, c) = map(int, input().split())
p_l = sorted(list(map(int, input().split())), reverse=True)[:x]
q_l = sorted(list(map(int, input().split())), reverse=True)[:y]
r_l = list(map(int, input().split()))
p_l = sorted(p_l + q_l + r_l, reverse=True)
print(sum(p_l[:x + y]))
