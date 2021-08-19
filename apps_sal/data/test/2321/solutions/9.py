def rs():
    return int(input())


def ri():
    return map(int, input().split())


def rli():
    return list(map(int, input().split()))


n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    ans = k - 1
    ans1 = 0
    while ans1 < k and s[ans1] == '<':
        ans1 += 1
    ans2 = 0
    while k - 1 - ans2 >= 0 and s[k - 1 - ans2] == '>':
        ans2 += 1
    ans = min([ans, ans2, ans1])
    print(ans)
