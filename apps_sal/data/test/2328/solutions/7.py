import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve2():
    n, k = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = float('inf')
    ans_x = -1
    for i in range(n - k):
        l = L[i]
        r = L[i + k]
        tmp = (r + l) // 2
        tmp_ans = max(r - tmp, tmp - l)
        if ans > tmp_ans:
            ans = tmp_ans
            ans_x = tmp
    print(ans_x)


n = int(input())
for _ in range(n):
    solve2()
