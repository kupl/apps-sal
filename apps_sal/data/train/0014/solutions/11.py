t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    (c, d) = list(map(int, input().split()))
    if a + c == b == d or a + d == b == c or b + c == a == d or (b + d == a == c):
        print('Yes')
    else:
        print('No')
