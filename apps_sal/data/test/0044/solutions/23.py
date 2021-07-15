'''input
5 2 1 4 5
'''

d, k, a, b, t = list(map(int, input().split()))

dist, time = min(d, k), min(d*a, k*a)

if dist < d:
    tstep = min(t+k*a, k*b)
    num_steps = (d-dist) // k
    time += num_steps * tstep
    dist += num_steps * k

    remaining = d - dist
    time += min(t + a*remaining, b*remaining)
print(time)


