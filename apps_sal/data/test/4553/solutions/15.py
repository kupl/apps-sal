a, b = map(int, input().split())
s = input()

if len(s) == a + b + 1 and s[a] == "-" and s.count("-") == 1:
    print("Yes")
else:
    print("No")
