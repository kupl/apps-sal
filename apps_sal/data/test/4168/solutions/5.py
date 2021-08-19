N = int(input())
max_digit = 34
bits = [0] * max_digit
sign = N > 0
if N < 0:
    N = -N
for i in range(N.bit_length()):
    if N >> i & 1:
        if i & 1 == sign:
            bits[i] += 1
            bits[i + 1] += 1
        else:
            bits[i] += 1
for i in range(max_digit):
    if bits[i] == 2:
        if bits[i + 1] == 1:
            bits[i] = 0
            bits[i + 1] = 0
        else:
            bits[i] = 0
            bits[i + 1] += 1
            bits[i + 2] += 1
res = ''
flg = False
for i in reversed(range(max_digit)):
    if not flg and bits[i] == 1:
        flg = True
        res += '1'
    elif flg:
        res += str(bits[i])
if res == '':
    res = '0'
print(res)
