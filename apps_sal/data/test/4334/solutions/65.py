(s, t) = input().split()
(a, b) = [int(i) for i in input().split()]
u = input()
if s == u:
    a -= 1
elif t == u:
    b -= 1
print(a, b)
