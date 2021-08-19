(k, s) = (int(input()), input())
print([s[:k] + '...', s][len(s) <= k])
