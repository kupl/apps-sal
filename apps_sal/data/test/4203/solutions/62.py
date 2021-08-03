S = input()
N = len(S)

if S[0] == "A" and S[2:N - 1].count("C") == 1 and sum(s.islower() for s in S) == N - 2:
    print("AC")
else:
    print("WA")
