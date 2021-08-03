a, b = map(int, input().split())
ans = ""

if a <= b:
    for i in range(b):
        ans += str(a)
elif b < a:
    for i in range(a):
        ans += str(b)

print(ans)
