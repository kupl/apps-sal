nv = list(map(int, input().split()))
n = nv[0] - 1
v = nv[1]
if v >= n:
    print(n)
    quit()
k = 2
money = v
while n - v > 0:
    n = n - 1
    money += k
    k += 1
print(money)
