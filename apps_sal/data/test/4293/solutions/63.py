p, q, r = list(map(int, input().split()))

a_c = p + q
a_b = r + q
b_c = p + r

minimum_time = min(a_c, a_b, b_c)

print(minimum_time)
