import sys

lines = []
for line in sys.stdin:
    lines.append(line)

n = int(lines[0].rstrip("\r\n\t "))

in_a = []
a_size = 0
a_sum = 0
b_sum = 0
for x in range(n, 0, -1):
    if a_sum <= b_sum:
        in_a.append(str(x))
        a_size += 1
        a_sum += x
    else:
        b_sum += x

print(("{}\n{} {}".format(
    abs(a_sum - b_sum),
    a_size,
    " ".join(in_a)
)))

