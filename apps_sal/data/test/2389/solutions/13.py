#!/usr/bin/env python3

n, a, b, c = map(int, input().split())
S = []
for _ in range(n):
    S.append(input())

ans = []
for i in range(n):
    if S[i] == "AB":
        if a == b == 0:
            print("No")
            return
        elif a < b or (a == b and i != n - 1 and "A" in S[i + 1]):
            ans.append("A")
            a += 1
            b -= 1
        else:
            ans.append("B")
            a -= 1
            b += 1
    elif S[i] == "BC":
        if b == c == 0:
            print("No")
            return
        elif c < b or (c == b and i != n - 1 and "C" in S[i + 1]):
            ans.append("C")
            c += 1
            b -= 1
        else:
            ans.append("B")
            c -= 1
            b += 1
    else:
        if c == a == 0:
            print("No")
            return
        elif c < a or (c == a and i != n - 1 and "C" in S[i + 1]):
            ans.append("C")
            c += 1
            a -= 1
        else:
            ans.append("A")
            c -= 1
            a += 1
print("Yes")
print("\n".join(ans))
return
