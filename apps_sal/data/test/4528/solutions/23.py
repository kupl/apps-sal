t = int(input())
for i in range(t):
    h, m = list(map(int, input().split()))
    print(24 * 60 - h * 60 - m)
