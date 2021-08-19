N = int(input())
if N == 0:
    s = '0'
else:
    s = ''
while N != 0:
    m = N % 2
    s += str(m)
    N = (N - m) * -1 // 2
print(s[::-1])
