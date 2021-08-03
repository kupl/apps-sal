t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    if(max(a, b) >= 2 * min(a, b)):
        print((min(a, b)))
    else:
        print(((a + b) // 3))
