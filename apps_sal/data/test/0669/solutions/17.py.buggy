import bisect
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a1, a2 = [], []
n1 = n // 2
app1 = a1.append
app2 = a2.append


def sums1(i, sum=0):
    if i == n1:
        app1(sum % m)
    else:
        sums1(i + 1, (sum + a[i]))
        sums1(i + 1, sum)


def sums2(i, sum=0):
    if i == n:
        app2(sum % m)
    else:
        sums2(i + 1, (sum + a[i]))
        sums2(i + 1, sum)


sums1(0)
sums2(n1)

ans = 0
end = len(a2) - 1

a1 = sorted(set(a1))
bis = bisect.bisect_left


def solve(i):
    nonlocal ans
    j = bis(a1, m - i)
    if ans < a1[j - 1] + i:
        ans = a1[j - 1] + i
    return ans


l = list(map(solve, a2))
print(l[-1])
