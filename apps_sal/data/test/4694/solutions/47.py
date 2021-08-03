def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    # print(a)
    for i in range(1, N, 1):
        ans += a[i] - a[i - 1]

    return ans


print((main()))
