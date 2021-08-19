(a, b, c) = map(int, input().split())
print('No' if a != b and b != c and (c != a) or (a == b and b == c) else 'Yes')
