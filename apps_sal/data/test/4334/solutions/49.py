(s, t) = input().split()
(a, b) = [int(x) for x in input().split()]
u = input()
if s == u:
    print(str(a - 1) + ' ' + str(b))
else:
    print(str(a) + ' ' + str(b - 1))
