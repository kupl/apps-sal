n, k, s, b = list(map(int, input().split()))
m = list(map(int, input().split()))
print(('Inc' if min(m) < s or max(m) > b or (max(m) != b) + (min(m) != s) > n - k else 'C') + 'orrect')
