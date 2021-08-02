A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

l = []
if A % 10 > 0:
    l.append(A % 10)
if B % 10 > 0:
    l.append(B % 10)
if C % 10 > 0:
    l.append(C % 10)
if D % 10 > 0:
    l.append(D % 10)
if E % 10 > 0:
    l.append(E % 10)

ans = len(l) * 10 + A + B + C + D + E - sum(l)
if len(l) > 0:
    ans += min(l) - 10
print(ans)
