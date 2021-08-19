n = int(input())
M = list(map(int, input().split()))
R = list(map(int, input().split()))


def nod(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


k = 1
for i in M:
    k = k * i // nod(k, i)
ans = 0
for D in range(k):
    for i in range(n):
        if D % M[i] == R[i]:
            ans += 1
            break
print(ans / k)
