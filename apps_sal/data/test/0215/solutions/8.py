def bitLenCount(x):
    length = 0
    count = 0
    while x:
        count += x & 1
        length += 1
        x >>= 1
    return count


n = input()
s = input()
msk = 0
ans = 0
for i in s:
    x = ord(i) - ord('a')
    if x >= 0 and x <= 25:
        msk |= 1 << x
    else:
        msk = 0
    ans = max(ans, bitLenCount(msk))
print(ans)
