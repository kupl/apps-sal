w, m = list(map(int, str.split(input())))
bits = [0] * 100
for i in range(100):

    m, bits[i] = divmod(m, w)

for i in range(99):

    if 1 < bits[i] < w - 1:

        print("NO")
        return

    if bits[i] == w - 1:

        bits[i] = 0
        bits[i + 1] += 1
        carry = 0
        for j in range(i + 1, 100):

            carry, bits[j] = divmod(bits[j] + carry, w)

print("YES")

