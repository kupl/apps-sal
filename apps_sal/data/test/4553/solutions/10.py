dg = "0123456789"

A, B = map(int, input().split())
S = input()

postcode = True
for i, ch in enumerate(S):
    if i == A:
        if ch != "-":
            postcode = False
            break
    else:
        if ch not in dg:
            postcode = False
            break

if postcode:
    print("Yes")
else:
    print("No")
