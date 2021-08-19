a, b = map(int, input().split())
s = str(input())
# print(s[a+1])

if s[a] == "-" and s.count("-") == 1:
    print("Yes")
else:
    print("No")
