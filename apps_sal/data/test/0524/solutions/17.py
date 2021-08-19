def solve(arr):
    arr.sort()
    c = 2
    ans = sum((v - 1 for v in arr))
    while True:
        cur = 1
        cur_ans = 0
        for v in arr:
            if cur - arr[-1] > ans:
                return ans
            cur_ans += abs(v - cur)
            cur *= c
        ans = min(ans, cur_ans)
        c += 1


n = int(input())
(*arr,) = list(map(int, input().split()))
print(solve(arr))
