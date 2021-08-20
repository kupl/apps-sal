n = int(input())
for i in range(n):
    (c, sum) = map(int, input().split())
    k = sum // c
    cnt1 = sum % c
    cnt2 = c - cnt1
    print(cnt1 * (k + 1) ** 2 + cnt2 * k ** 2)
