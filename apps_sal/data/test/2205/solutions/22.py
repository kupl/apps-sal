def com(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


n = int(input())
lis = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    a = com(i - 1)
    rem = n % i
    b = com(rem)
    if n // i % 2 == 1:
        ans ^= a ^ b ^ lis[i - 1]
    else:
        ans ^= b ^ lis[i - 1]
print(ans)
