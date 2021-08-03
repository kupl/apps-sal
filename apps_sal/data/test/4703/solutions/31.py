def hojyu(a):
    if len(a) != N:
        return "0" * (N - len(a)) + a
    else:
        return a


S = input()
N = len(S) - 1
R = list()
ans = 0
for i in range(2**N):
    s = str(bin(i)[2:])
    s = hojyu(s)
    b = 0
    mae = 0
    for k in range(len(s)):
        if s[k] == "1":
            b += int(S[mae:k + 1])
            mae = k + 1
    b += int(S[mae:])
    ans += b
print(ans)
