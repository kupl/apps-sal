a, b, c = map(int, input().split())
if c < a:
    print("NO")
else:
    if c > a + b:
        print("NO")
    else:
        print("YES")
