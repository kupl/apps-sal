n = int(input())
le = n
if n % 2 == 1:
    le -= 1
lo = n
if n % 2 == 0:
    lo -= 1


def f(fir, las):
    fir = int(fir)
    las = int(las)
    return (fir + las) * ((las - fir) // 2 + 1) // 2


print(f(2, le) - f(1, lo))
