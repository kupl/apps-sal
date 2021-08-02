c, d = list(map(int, input().split(" ")))
n, m = list(map(int, input().split(" ")))
k = int(input())
mini = n * m - k
if mini < 1:
    print(0)
elif d * n <= c:  # easier one at a time
    print(d * mini)
else:
    total = (mini // n) * c
    mini = mini % n
    total += min(c, d * mini)
    print(total)
