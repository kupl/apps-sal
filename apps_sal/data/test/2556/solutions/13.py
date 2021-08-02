n = int(input())

for i in range(n):
    ans = 0
    num, m = list(map(int, input().split()))
    tmp = m // num
    add = m % num
    tmp2 = num - add
    ans = tmp ** 2 * tmp2 + (tmp + 1) ** 2 * add
    print(ans)
