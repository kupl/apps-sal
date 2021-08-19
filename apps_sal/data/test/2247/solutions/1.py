t = int(input())
for i in range(t):
    (s, a, b, c) = map(int, input().split())
    x = s // c
    print(s // c + x // a * b)
