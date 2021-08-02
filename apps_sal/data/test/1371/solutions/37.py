s = int(input())

mod = 1000000007

d = [1, 0, 0]

for i in range(s - 2):
    d = [d[1], d[2], (d[0] + d[2]) % mod]

print((d[2]))
