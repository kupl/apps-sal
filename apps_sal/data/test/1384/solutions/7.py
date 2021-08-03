def read_ints():
    return [int(i) for i in input().split()]


n = int(input())
s = read_ints()
to_rem = n if sum(s) else 0
for i in range(n):
    to_rem = min(to_rem, s[:i].count(1) + (s[i:].count(0) if sum(s[i:]) else 0))

print(n - to_rem)
