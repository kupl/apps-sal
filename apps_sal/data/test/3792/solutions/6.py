n, k = list(map(int, input().split()))
s = input()
t = input()
Sum = -1
pos = 0
ans = 0
while pos < n and s[pos] == t[pos]:
    pos += 1
    ans += 1
for i in range(pos, n):
    Sum = Sum * 2 + 1 - ord(s[i]) + ord(t[i])
    if Sum + 2 >= k:
        ans += (n - i) * k
        break
    else:
        ans += Sum + 2
print(ans)
