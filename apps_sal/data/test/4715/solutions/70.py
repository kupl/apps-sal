a, b, c = map(int, input().split())
if a == b and b == c:
    print(1)
elif a != b and b != c and c != a:
    print(3)
else:
    print(2)
