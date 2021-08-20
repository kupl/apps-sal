s = int(input())
mod = 1000000007
d = [0] * (s + 1)
d[0] = 1
sum = 0
for i in range(s + 1):
    if 3 <= i:
        sum += d[i - 3]
        sum %= mod
    d[i] += sum
print(d[s])
