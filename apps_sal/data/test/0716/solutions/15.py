n, a, b = list(map(int, input().split()))
s = input()
if s[a-1] == s[b-1] or a == b:
    print(0)
else:
    print(1)

