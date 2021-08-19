N = int(input())
li = list(map(int, input().split()))
M = int(input())
an = sum(li)
for i in range(M):
    (p, x) = map(int, input().split())
    h = x - li[p - 1]
    print(sum(li) + h)
