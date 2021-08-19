n, m = map(int, input().split())
print(*['#' * -~-~m] + ['#' + input() + '#' for _ in range(n)] + ['#' * -~-~m], sep='\n')
