from sys import stdin
input = stdin.readline
n = int(input())
(s1, s2) = (input(), input())
mod = 1000000007
flag1 = flag2 = flag3 = ans1 = ans2 = ans3 = cnt = 1
for i in range(n):
    if s1[i] == '?' and s2[i] == '?':
        ans1 *= 55
        ans2 *= 55
        ans3 *= 10
        cnt *= 100
    elif s1[i] == '?':
        ans1 *= 10 - int(s2[i])
        ans2 *= int(s2[i]) + 1
        cnt *= 10
    elif s2[i] == '?':
        ans2 *= 10 - int(s1[i])
        ans1 *= int(s1[i]) + 1
        cnt *= 10
    elif s1[i] < s2[i]:
        flag1 = flag3 = 0
    elif s1[i] > s2[i]:
        flag2 = flag3 = 0
    cnt %= mod
    ans1 %= mod
    ans2 %= mod
    ans3 %= mod
print(cnt - (ans1 * flag1 + ans2 * flag2 - ans3 * flag3) % mod)
