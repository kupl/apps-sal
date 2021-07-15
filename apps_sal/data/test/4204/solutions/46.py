import sys, math
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
s = lines.pop(0)
k, = [int(num) for num in lines.pop(0).split(" ")]
days = 5000 * (10 ** 12)
for n in s:
    log_k = math.log10(k)
    n = int(n)
    log_n_days = math.log10(n) * days
    if log_k > log_n_days:
        k -= n ** days
    else:
        break
print(n)

