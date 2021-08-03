n = int(input())
a = [int(i) for i in input().split()]
s = xor = 0
right = 0
ans = 0
for left in range(n):
    while right < n and s + a[right] == xor ^ a[right]:
        s += a[right]
        xor ^= a[right]
        right += 1
    ans += right - left
    if left == right:
        right += 1
    else:
        s -= a[left]
        xor ^= a[left]
print(ans)
