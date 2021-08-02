N = int(input())

T, A = map(int, input().split())

for i in range(N - 1):
    t, a = map(int, input().split())
    da = (a - A % a) % a
    dt = (A + da) * t // a - T
    if dt >= 0:
        A += da
        T += dt
    else:
        i = -(dt // t)
        da += i * a
        dt += i * t
        A += da
        T += dt

print(T + A)
