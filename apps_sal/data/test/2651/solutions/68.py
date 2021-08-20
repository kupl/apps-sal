(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
'\n各辺を独立して組み合わせて良い。\nどのxの辺もすべてのyの辺をかけて合計することから、\n分配法則を適用して\nans = (xの取りうる辺の総和)x(yの取りうる辺の総和)\nとなる\nしたがって、各辺の総和を効率的に求められれば良い\n一旦xに着目し、各点の組合せでできる辺の総和を求める。\nここで、x_iとx_i+1の区間は他の辺の部分としてカウントされる回数は\n(i+1)*(n-i-1) 0-indexed\nしたがって、差数列に回数を畳みこんで辺の総和が求まる\nyも同様に総和を求め、積を取れば良い\n'
x_diff = [x[i] - x[i - 1] for i in range(1, n)]
y_diff = [y[i] - y[i - 1] for i in range(1, m)]
x_sum = 0
for (i, dx) in enumerate(x_diff):
    x_sum = (x_sum + dx * (i + 1) * (n - i - 1) % mod) % mod
y_sum = 0
for (i, dy) in enumerate(y_diff):
    y_sum = (y_sum + dy * (i + 1) * (m - i - 1) % mod) % mod
print(x_sum * y_sum % mod)
