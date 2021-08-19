(s, t) = map(str, input().split())
(a, b) = map(int, input().split())
u = input()
if u == t:
    b -= 1
else:
    a -= 1
print(a, b)
