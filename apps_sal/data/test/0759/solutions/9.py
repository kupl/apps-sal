def div(a, b):
    return a // b + int(a % b != 0)

hh, mm = list(map(int, input().split()))
h, d, c, n = list(map(int, input().split()))
wait = 0
if hh < 20:
    wait = 60 * (20 - hh - 1) + 60 - mm
print(0.2 * min(div(h, n) * c * 5, div(wait * d + h, n) * c * 4))

