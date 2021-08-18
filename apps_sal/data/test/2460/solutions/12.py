n, m = [int(x) for x in input().split()]
xs = [int(x) for x in input().split()]
ts = [int(x) for x in input().split()]


taxi_idx = sorted([xs[idx] for idx in range(n + m) if ts[idx] == 1])
passenger_idx = sorted([xs[idx] for idx in range(n + m) if ts[idx] == 0])

a_is = [0] * len(taxi_idx)
t_idx = 0
p_idx = 0

while True:
    if p_idx >= len(passenger_idx):
        break

    if t_idx == len(taxi_idx) - 1:
        a_is[t_idx] += 1
    else:
        while t_idx < len(taxi_idx) - 1:
            d1 = abs(passenger_idx[p_idx] - taxi_idx[t_idx])
            d2 = abs(passenger_idx[p_idx] - taxi_idx[t_idx + 1])
            if d1 > d2:
                t_idx += 1
            else:
                break

        a_is[t_idx] += 1

    p_idx += 1

print(' '.join([str(x) for x in a_is]))
