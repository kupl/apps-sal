x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

L = P[:x] + Q[:y] + R
L.sort(reverse=True)
print(sum(L[:x+y]))
