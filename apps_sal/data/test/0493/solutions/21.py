(n, prev, prch, val) = (int(input()), -1, 'L', 0)
for (i, d) in enumerate(input()):
    if d == 'L':
        if prev != -1 and (i - prev) % 2 == 0:
            val += 1
        (prev, prch) = (i, d)
    elif d == 'R':
        val += i - prev - 1
        (prev, prch) = (i, d)
if prch == 'L':
    val += n - prev - 1
print(val)
