(n, k) = map(int, input().split())
k -= 1
go_to_border = min(k, n - k - 1)
more = 3 * n
print(go_to_border + more)
