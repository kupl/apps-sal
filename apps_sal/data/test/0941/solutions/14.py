(b, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(k):
    if i == k - 1:
        ans ^= a[i] % 2
    else:
        ans ^= a[i] % 2 * (b % 2)
print('even' if ans == 0 else 'odd')
