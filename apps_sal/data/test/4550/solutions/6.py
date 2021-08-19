(a, b, c) = sorted(map(int, input().split()), reverse=True)
print('Yes') if a == b + c else print('No')
