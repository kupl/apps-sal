n, m = list(map(int, input().split()))
s1 = input()
s2 = input()
if m < n:
    s2 = "0" * (n - m) + s2
    m = n
else:
    s1 = "0" * (m - n) + s1
    n = m

# print(s1,s2)
#count1 = s1.count("1");
#count2 = s2.count("1");
ans = [0] * n
for i in range(n):
    if s2[i] == "1":
        ans[i] = 1
for i in range(1, n):
    ans[i] += ans[i - 1]


mod = 998244353
final = 0
n -= 1
# print(s1)
# print(*ans)
for i in range(m):
    if s1[i] == "1":
        # print(i)
        final += (pow(2, n - i, mod) * ans[i]) % mod
        final %= mod
print(final)
