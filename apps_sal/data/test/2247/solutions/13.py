t = int(input())
for q in range(t):
    (s, a, b, c) = list(map(int, input().split()))
    print(s // c + s // c // a * b)
