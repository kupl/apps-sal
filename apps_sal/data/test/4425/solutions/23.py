N, K = map(int, input().split())


def func1(i, k):
    ans = 0
    num = i
    end = False
    if num >= k:
        return 0
    while(not end):
        ans += 1
        num *= 2
        if num >= k:
            end = True
            break
    return ans


ans = 0
for initial_score in range(1, N + 1):
    ans += (1 / N) * (1 / 2) ** func1(initial_score, K)
print(ans)
