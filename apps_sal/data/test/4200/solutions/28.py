n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
sorted_A = list(reversed(sorted(A)))
print(("No" if sorted_A[m - 1] < sum(A) / (4 * m) else "Yes"))
