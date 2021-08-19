def solve():
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c <= 0:
                break
            else:
                ans += 1
    return ans


n = int(input())
print(solve())
