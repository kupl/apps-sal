n = int(input())
t = input()
ans = 0

s = "110" * 10**6


if s[0:n] == t:
    ans += 10**10 - (n - 1) // 3
    # if n%3 == 0:
    #     ans += 1

if s[1:n + 1] == t:
    ans += 10**10 - n // 3
    # if n%3 == 0:
    #     ans += 1

if s[2:n + 2] == t:
    ans += 10**10 - (n + 1) // 3
    # if n%3 == 0:
    #     ans += 1

print(ans)
