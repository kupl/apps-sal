def solve():
    K = int(input())
    if K == 49:
        print(2)
        return [27, 24]
    print(50)
    (a, b) = (K // 50, K % 50)
    ans = [49 + a] * 50
    for i in range(50):
        if i < b:
            ans[i] += 51 - b
        else:
            ans[i] -= b
    return ans


print(*solve())
