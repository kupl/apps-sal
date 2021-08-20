N = int(input()) - 1
keta = 1
cumsum = 0
oldcumsum = 0
while True:
    cumsum += 26 ** keta
    if cumsum > N:
        break
    else:
        oldcumsum = cumsum
    keta += 1
N -= oldcumsum
name = ''
for k in range(1, keta + 1):
    ch_n = N // 26 ** (keta - k)
    ch = chr(ord('a') + ch_n)
    name += ch
    N -= ch_n * 26 ** (keta - k)
print(name)
