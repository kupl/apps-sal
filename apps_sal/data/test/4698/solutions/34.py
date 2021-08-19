n = int(input())
l = list(map(int, input().split()))
m = int(input())
sum_l = sum(l)
for i in range(m):
    (p, x) = list(map(int, input().split()))
    ans = sum_l - l[p - 1] + x
    print(ans)
