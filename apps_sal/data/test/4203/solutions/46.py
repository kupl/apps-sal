S = str(input())
ans = "WA"
if S[0] == "A":
    if "C" in S[2:-1] and S.count("C") == 1:
        x = S.index("C")
        S = S[0].lower() + S[1:x] + S[x].lower() + S[x + 1:]
        if S == S.lower():
            ans = "AC"
print(ans)
