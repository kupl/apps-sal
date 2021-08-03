S = input()
r = "WA"
n = len(S)
l = list(S)

if S[0] == "A" and S[2:n - 1].count('C') == 1:
    s = S.replace('A', 'p').replace('C', 'p')
    if s.islower():
        r = 'AC'
print(r)
