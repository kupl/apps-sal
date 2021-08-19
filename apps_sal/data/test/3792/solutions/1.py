(n, k) = map(int, input().split())
(s, t, cu) = (input(), input(), [1])
for i in range(n):
    cu += [cu[-1] * 2 - (s[i] == 'b') - (t[i] == 'a')]
    if cu[-1] >= k:
        cu[-1] = k
        break
print(sum(cu) + (n - i - 1) * k - 1)
