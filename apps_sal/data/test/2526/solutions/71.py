(x, y, a, b, c) = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R = R + P[:x] + Q[:y]
R.sort(reverse=True)
print(sum(R[:x + y]))
