n, k = map(int, input().split())
A = tuple(map(int, input().split()))
ones = [0] * k.bit_length()
for a in A:
    for i in range(k.bit_length()):
        ones[i] += (a >> i) & 1

x = 0
for idx, one in enumerate(ones[::-1]):
    if n - one > one:
        xx = 2**(len(ones) - 1 - idx)
        if x + xx > k:
            continue
        else:
            x += xx
ans = 0
for a in A:
    ans += a ^ x
print(ans)
