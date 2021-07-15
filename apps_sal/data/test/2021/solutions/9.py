n = int(input())
l = list(map(int, input().split()))
k = int(input())
m = list(map(int, input().split()))
l.sort(reverse=1)
sm = sum(l)
for i in m:
    print(sm - l[i - 1])

