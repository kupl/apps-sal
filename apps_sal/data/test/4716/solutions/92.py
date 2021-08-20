(n, k) = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
print(sum(lst[-1 * k:]))
