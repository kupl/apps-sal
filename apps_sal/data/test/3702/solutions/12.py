(_, a, d) = list(map(int, input().split()))
ten_k = 10 ** 9
n = 12 * ten_k
t_inv = 1114945049
u = 125 * a * t_inv % ten_k
v = 125 * d * t_inv % ten_k
b = u * n + 1
e = v * n
print(b, e)
