def f(m):
    ans = 0
    for i in range(len(a)):
        ans += m % a[i]
    return ans


n = int(input())
a = list(map(int, input().split()))

print(sum(a) - n)
