import math


def slog(x): return math.log(math.log(x))


a = [float(n) for n in input().split()]
r = ([(lambda x, y, z: -10.0**10 if math.log(x) <= 0 else slog(x) + z * math.log(y), "x^y^z"),
      (lambda x, y, z:-10.0**10 if math.log(x) <= 0 else slog(x) + y * math.log(z), "x^z^y"),
      (lambda x, y, z:-10.0**10 if math.log(x) <= 0 else slog(x) + math.log(y) + math.log(z), "(x^y)^z"),
      (lambda x, y, z:-10.0**10 if math.log(y) <= 0 else slog(y) + z * math.log(x), "y^x^z"),
      (lambda x, y, z:-10.0**10 if math.log(y) <= 0 else slog(y) + x * math.log(z), "y^z^x"),
      (lambda x, y, z:-10.0**10 if math.log(y) <= 0 else slog(y) + math.log(z) + math.log(x), "(y^x)^z"),
      (lambda x, y, z:-10.0**10 if math.log(z) <= 0 else slog(z) + y * math.log(x), "z^x^y"),
      (lambda x, y, z:-10.0**10 if math.log(z) <= 0 else slog(z) + x * math.log(y), "z^y^x"),
      (lambda x, y, z:-10.0**10 if math.log(z) <= 0 else slog(z) + math.log(y) + math.log(x), "(z^x)^y")])
rr = ([(lambda x, y, z: y**z * math.log(x), "x^y^z"),
      (lambda x, y, z: z**y * math.log(x), "x^z^y"),
      (lambda x, y, z: math.log(x) * y * z, "(x^y)^z"),
      (lambda x, y, z: math.log(y) * x**z, "y^x^z"),
      (lambda x, y, z: math.log(y) * z**x, "y^z^x"),
      (lambda x, y, z: math.log(y) * z * x, "(y^x)^z"),
      (lambda x, y, z: math.log(z) * x ** y, "z^x^y"),
      (lambda x, y, z: math.log(z) * y ** x, "z^y^x"),
      (lambda x, y, z: math.log(z) * x * y, "(z^x)^y")])
exp = ""
best = -10**50
if all([x <= 1.0 for x in a]):
    for f, e in rr:
        val = f(a[0], a[1], a[2])
        if val - best > 1e-10:
            best = val
            exp = e

else:
    for f, e in r:
        val = f(a[0], a[1], a[2])
        if val > best:
            best = val
            exp = e

print(exp)
