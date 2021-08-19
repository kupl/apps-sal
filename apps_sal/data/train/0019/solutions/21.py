def solve(n, k, d, a):
    m = {}
    s = list(set(a))
    ans = float('inf')
    for i in s:
        m[i] = 0
    sm = 0
    for i in range(d):
        m[a[i]] += 1
        if m[a[i]] == 1:
            sm += 1
    ans = sm
    for i in range(d, n):
        x = a[i - d]
        y = a[i]
        m[x] -= 1
        if m[x] == 0:
            sm -= 1
        if m[y] == 0:
            sm += 1
        m[y] += 1
        ans = min(ans, sm)
    return ans


def main():
    t = int(input())
    for i in range(t):
        (n, k, d) = list(map(int, input().split()))
        a = list(map(int, input().split()))
        print(solve(n, k, d, a))


main()
