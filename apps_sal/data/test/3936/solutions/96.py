n = int(input())
s = input()
t = input()
prev = -1
i = 0
ans = 1
mod = pow(10,9)+7
while i != n:
    if s[i] == t[i]:
        if prev == -1:
            ans *= 3
        elif prev == 0:
            ans *= 2
        prev = 0
        i += 1
    else:
        if prev == -1:
            ans *= 6
        elif prev == 0:
            ans *= 2
        else:
            ans *= 3
        prev = 1
        i += 2
    ans %= mod
print(ans)
