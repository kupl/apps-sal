n = int(input())
a = list(map(int, input().split()))
ans = 0
k = 0
Xor = 0
Add = 0
for i in range(n):
    while k < n and Xor ^ a[k] == Add + a[k]:
        Xor ^= a[k]
        Add += a[k]
        k += 1
    ans += k - i
    Xor ^= a[i]
    Add -= a[i]
print(ans)
