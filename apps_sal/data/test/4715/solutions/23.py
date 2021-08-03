a, b, c = map(int, input().split())

if a == b and b == c:
    ans = 1
elif a == b and b != c:
    ans = 2
elif a != b and b == c:
    ans = 2
elif a == c and a != b:
    ans = 2
else:
    ans = 3
print(ans)
