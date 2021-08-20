n = int(input())
li = list(map(int, input().split()))
m = int(input())
c = sum(li)
for i in range(m):
    (a, b) = map(int, input().split())
    print(c - li[a - 1] + b)
