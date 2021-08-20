t = int(input())
for i in range(t):
    hh = 23
    mm = 60
    (h, m) = list(map(int, input().split()))
    print((hh - h) * 60 + mm - m)
