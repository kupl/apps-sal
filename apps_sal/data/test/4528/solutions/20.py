q = int(input())
for i in range(q):
    h, m = list(map(int, input().split()))
    print(24 * 60 - h * 60 - m)
