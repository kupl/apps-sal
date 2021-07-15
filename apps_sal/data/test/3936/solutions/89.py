n = int(input())
s1 = input()
s2 = input()
mod = 10**9+7
ans = 1
i = 0
prev = "None"
while i<n:
    if s1[i] == s2[i]:
        if prev == "None":
            ans = 3
        elif prev == "X":
            ans = ans*2%mod
        else:
            pass
        i += 1
        prev = "X"
    else:
        if prev == "None":
            ans = 6
        elif prev == "X":
            ans = ans*2%mod
        else:
            ans = ans*3%mod
        i += 2
        prev = "Y"
print(ans)

