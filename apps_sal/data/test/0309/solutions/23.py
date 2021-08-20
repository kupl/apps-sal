(n, m) = list(map(int, input().split()))
n = str(bin(n))[2:]
m = str(bin(m))[2:]
n = '0' * (len(m) - len(n)) + n
f = 0
for i in range(len(n)):
    if n[i] == '0' and m[i] == '1':
        print(2 ** (len(n) - i) - 1)
        f = 1
        break
if not f:
    print(f)
