def f():
    return input()


(a, b) = list(map(int, f().split()))
c = 0
while a != b and a != 0 and (b != 0):
    lo = min(a, b)
    hi = max(a, b)
    a = hi % lo
    b = lo
    c += int(hi / lo)
print(c)
