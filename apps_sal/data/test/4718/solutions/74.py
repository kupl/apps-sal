S = str(input())
s = "2"
for i in range(1, 10):
    if i == 3:
        s += "8"
    else:
        s += S[i]
print(s)
