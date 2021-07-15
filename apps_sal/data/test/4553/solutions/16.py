a, b = map(int, input().split())
s = input()
if s[a] == "-" and s.count("-") == 1:
    print("Yes")
else:
    print("No")
