(n, p) = [int(a) for a in input().strip().split(' ')]
e = [int(a) for a in input().strip().split(' ')]
max_sum = 0
s = sum(e)
current_s = 0
for i in e:
    current_s += i % p
    current_s %= p
    max_sum = max(max_sum, current_s + (s - current_s) % p)
print(max_sum)
