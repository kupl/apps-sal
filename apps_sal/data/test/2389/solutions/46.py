import sys
n, a, b, c = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
    
ans =[]
for i in range(n):
    if s[i] == "AB":
        if a == b == 1 and i < n-1:
            if s[i+1] == "AC":
                a += 1
                b -= 1
                ans.append("A")
            else:
                a -= 1
                b+= 1
                ans.append("B")
        else:
            if min(a, b) == a:
                a += 1
                b -= 1
                ans.append("A")
            else:
                a -= 1
                b+= 1
                ans.append("B")
    elif s[i] == "BC":
        if c == b == 1 and i < n-1:
            if s[i+1] == "AB":
                b += 1
                c -= 1
                ans.append("B")
            else:
                b -= 1
                c+= 1
                ans.append("C")
        else:
            if min(c, b) ==b:
                b += 1
                c -= 1
                ans.append("B")
            else:
                b -= 1
                c+= 1
                ans.append("C")
    else:
        if c == a == 1 and i < n-1:
            if s[i+1] == "BC":
                c += 1
                a -= 1
                ans.append("C")
            else:
                a += 1
                c-= 1
                ans.append("A")
        else:
            if min(c, a) == c:
                c += 1
                a -= 1
                ans.append("C")
            else:
                c -= 1
                a += 1
                ans.append("A")
    if min(a, b, c) < 0:
        print("No")
        return

print("Yes")
print("\n".join(ans))
