(n, k) = list(map(int, input().split()))
s = input()
d = [0] * 26
for i in range(n):
    d[ord(s[i]) - 65] += 1
d.sort()
ans = 0
while k > 0:
    if k < d[-1]:
        ans += k * k
        break
    else:
        k -= d[-1]
        ans += d[-1] * d[-1]
        d.pop()
print(ans)
    

