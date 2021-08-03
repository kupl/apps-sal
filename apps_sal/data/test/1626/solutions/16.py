n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = n // k
ans = 1
for i in range(c):
    t_ans = ((10**k - 1) // a[i] + 1) + (b[i] * 10**(k - 1)) // a[i] - ((b[i] + 1) * 10**(k - 1)) // a[i]
    if (b[i] * 10**(k - 1)) % a[i] == 0:
        t_ans -= 1
    if ((b[i] + 1) * 10**(k - 1)) % a[i] == 0:
        t_ans += 1
    ans *= t_ans
    ans = ans % (10**9 + 7)
print(ans)
