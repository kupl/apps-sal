A, B, C = list(map(int, input().split()))
sev = 0
fiv = 0

if A == 7:
    sev += 1
elif A == 5:
    fiv += 1
if B == 7:
    sev += 1
elif B == 5:
    fiv += 1
if C == 7:
    sev += 1
elif C == 5:
    fiv += 1
if sev == 1 and fiv == 2:
    print("YES")
else:
    print("NO")
