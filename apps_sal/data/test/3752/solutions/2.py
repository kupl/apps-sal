(k, d, t) = [int(x) for x in input().split()]
tt = t * 2
t_loop = ((k - 1) // d + 1) * d
amount = k * 2 + (t_loop - k)
n_loop = tt // amount
rem = tt % amount
if rem <= k * 2:
    print(n_loop * t_loop + rem / 2)
else:
    print(n_loop * t_loop + rem - k)
