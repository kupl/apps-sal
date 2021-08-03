x = int(input())
ans = []
t = 0
while x != 2 ** x.bit_length() - 1:
    if t % 2:
        x += 1
    else:
        xb = x.bit_length()
        ans.append(xb)
        x ^= 2 ** xb - 1
    t += 1
print(t)
print(*ans)
