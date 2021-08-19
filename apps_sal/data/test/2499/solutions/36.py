3.6
n = int(input())
a = [int(item) for item in input().split()]
aor = 0
axor = 0
for item in a:
    aor |= item
    axor ^= item
rank = 0
ans = 0
for bit in range(61):
    if axor & 1 << 60 - bit:
        ans += 1 << 60 - bit
        continue
    found_in_bit = False
    for i in range(rank, n):
        if a[i] & 1 << 60 - bit:
            if not found_in_bit:
                (a[rank], a[i]) = (a[i], a[rank])
                for j in range(rank):
                    if a[j] & 1 << 60 - bit:
                        a[j] ^= a[rank]
                found_in_bit = True
                rank += 1
            else:
                a[i] ^= a[rank - 1]
        else:
            continue
ret = 0
for item in a:
    ret ^= item & ~axor
ans += ret * 2
print(ans)
