N = int(input())
M = []
A = []
R = []
C = []
H = []
for _ in range(N):
    s = input()
    if s.startswith("M"):
        M.append(s)
    if s.startswith("A"):
        A.append(s)
    if s.startswith("R"):
        R.append(s)
    if s.startswith("C"):
        C.append(s)
    if s.startswith("H"):
        H.append(s)

m = len(M)
a = len(A)
r = len(R)
c = len(C)
h = len(H)
ans = m*a*r + m*a*c + m*a*h + m*r*c + m*r*h + m*c*h + a*r*c + a*r*h + a*c*h + r*c*h
print(ans)
