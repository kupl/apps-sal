a, b, c, d = map(int, input().split())
print('Yes' if any([all([abs(a-b) <= d, abs(b-c)<= d]), abs(a-c) <= d]) else 'No')
