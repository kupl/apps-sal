n = int(input())
w_fr = []
h_fr = []
c = 0
b = 0
itog = ""
d = 0

for i in range(n):
    w, h = map(int, input().split(" "))
    w_fr.append(w)
    h_fr.append(h)
    d += w

h_minus_max, h_max = sorted(h_fr)[-2:]

for i in range(n):
    b = d - w_fr[i]
    if h_max == h_fr[i]:
        itog += str(h_minus_max * b) + " "
    else:
        itog += str(h_max * b) + " "
    c = 0
    b = 0

print(itog[:-1])
