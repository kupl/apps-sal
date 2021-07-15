n = int(input())
f = lambda x: n // x
a1 = f(2) + f(3) + f(5) + f(7)
a2 = f(6) + f(10) + f(14) + f(15) + f(21) + f(35)
a3 = f(30) + f(42) + f(70) + f(105)
a4 = f(210)
ans = n - (a1 - a2 + a3 - a4)
print(ans)

