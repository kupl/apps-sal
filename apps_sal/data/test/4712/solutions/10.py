(H, W) = map(int, input().split())
L = ['#' + input() + '#' for _ in range(H)]
L = ['#' * (W + 2)] + L + ['#' * (W + 2)]
[print(i) for i in L]
