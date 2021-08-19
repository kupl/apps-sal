(a, b, c) = map(int, input().split())
print('No' if a == b == c or (a != b and b != c and (c != a)) else 'Yes')
