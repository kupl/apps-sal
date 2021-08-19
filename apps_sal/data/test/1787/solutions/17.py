S = input()
mod = 10**9 + 7

ANS = 0
YET = 0
OK = 0

for s in S:
    if s == "a":
        YET += (OK + 1) % mod
        ANS = (ANS + OK + 1) % mod

    elif s == "b":
        OK = (OK + YET) % mod
        YET = 0

    # print(YET,OK,ANS)

print(ANS)
