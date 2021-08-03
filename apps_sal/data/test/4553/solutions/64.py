a, b = (int(i) for i in input().split())
s = input()
if '-' not in s[:a] and s[a] == '-' and '-' not in s[a + 1:]:
    print("Yes")
else:
    print("No")
