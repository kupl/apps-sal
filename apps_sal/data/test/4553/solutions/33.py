a, b = map(int, input().split())
s = input()

if s[a] == "-" and len(s) == a + b + 1 and "-" not in s[:a] and "-" not in s[a + 1:]:
    print("Yes")
else:
    print("No")
