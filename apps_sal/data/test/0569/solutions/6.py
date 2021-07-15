n = int(input())

s = input()

x = len(s) - len(set(s))

if len(set(s)) + x > 26:
    print(-1)
else:
    print(x)

