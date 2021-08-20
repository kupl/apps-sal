S = input().strip().strip('0')
print(['NO', 'YES'][S == S[::-1]])
