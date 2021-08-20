t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    ans = (23 - a) * 60 + (60 - b)
    print(ans)
