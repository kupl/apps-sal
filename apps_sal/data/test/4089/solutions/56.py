N = int(input())

S = 0
Length = 0
count = 0
for i in range(1, 99):
    count += 1
    S += 26**i
    Length += 1
    if N <= S:
        break
k = N - S + 26**count
x = k - 1
ans = ""
for i in range(Length):
    r = x % 26
    ans += chr(ord("a") + r)
    q = x // 26
    x = q

print(ans[:: -1])
