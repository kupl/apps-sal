n = int(input())
T = list(map(int, input().split()))
m = int(input())

sum_T = sum(T)

for i in range(m):
    p, x = list(map(int, input().split()))
    ans = sum_T - T[p - 1] + x
    print(ans)
