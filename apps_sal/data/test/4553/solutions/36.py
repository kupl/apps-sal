a,b = map(int, input().split())
s = input()

if ("-" not in s[:a])&("-" not in s[a+1:])&(s[a]=="-"):
    print("Yes")
else:
    print("No")
