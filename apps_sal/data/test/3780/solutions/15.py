f = lambda: list(map(int, input().split()))



abs = lambda q: q[0] * q[0] + q[1] * q[1]

dot = lambda: v[0] * d[0] + v[1] * d[1]

get = lambda a, b, c: (b - (b * b - a * c) ** 0.5) / a



p = f()

d = [p[k + 2] - p[k] for k in [0, 1]]

v, t = f()

s = v * v



v = f()

i = get(abs(v) - s, dot(), abs(d))

d = [d[k] - t * v[k] for k in (0, 1)]



v = f()

j = get(abs(v) - s, dot() + t * s, abs(d) - t * t * s)



print(i if i < t else t + j)



# Made By Mostafa_Khaled

