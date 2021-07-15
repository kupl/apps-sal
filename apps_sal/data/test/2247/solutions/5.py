n = int(input())
for i in range(n):
    s, a, b, c = map(int, input().split())
    ans = s // c + (s // c) // a * b
    print(ans)
