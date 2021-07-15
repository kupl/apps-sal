T = int(input())
for __ in range(T):
    a, b = map(int, input().split())
    c = min((a + b) // 3, a, b)
    print(c)
