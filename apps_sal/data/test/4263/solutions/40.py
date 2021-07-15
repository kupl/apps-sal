S = input()
T = []

for i in range(len(S)):
    s = S[i]
    if (s == "A")or(s == "T")or(s == "C")or(s == "G"):
        T.append(0)
    else:
        T.append(1)

point = [0]*(len(S)+1)

for i in range(len(S)):
    if T[i] == 0:
        point[i+1]=point[i]+1
    else:
        point[i+1]=0

print((max(point)))

