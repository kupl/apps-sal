n = int(input())
a = list(map(int, input().split()))
def solve(a):
    ans = 1
    if 0 in a:
        return 0
    for i in a:
        ans *= i
        if ans > pow(10, 18):
            return -1
    return ans
ans = solve(a)
print(ans)
