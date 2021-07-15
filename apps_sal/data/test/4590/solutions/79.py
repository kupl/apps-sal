N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def get_integral(nums):
    integral = [0]
    for i in range(0, len(nums)):
        integral.append(integral[i] + nums[i])

    return integral


integral_a = get_integral(A)
integral_b = get_integral(B)

ans = 0
bestj = M
for i in range(N+1):
    ta = integral_a[i]
    if ta > K:
        break
    while ta + integral_b[bestj] > K:
        bestj -= 1

    best = i + bestj
    ans = max(best, ans)

print(ans)



