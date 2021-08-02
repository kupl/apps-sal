a, b, c = list(map(int, input().split()))

if a == b:
    ans = c
elif b == c:
    ans = a
else:
    ans = b
print(ans)
