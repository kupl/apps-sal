# https://codeforces.com/contest/1265/problem/B

def main():
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(n):
        idx[p[i]-1] = i
    ans = ''
    left = n
    right = 0
    for i in range(n):
        left = min(left, idx[i])
        right = max(right, idx[i])
        if right - left == i:
            ans += '1'
        else:
            ans += '0'
    return ans

t = int(input())
for i in range(t):
    print(main())

