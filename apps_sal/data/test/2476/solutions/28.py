from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lst = [0] * (N + 1)
for a in A:
    lst[a - 1] += 1
lst.sort()  # 頻度列

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + lst[i + 1]

# print (lst)
# print (s)


def check(x, k):
    i = bisect_left(lst, x) - 1
    total = x * (N - i) + s[i]
    return total >= x * k


ans = N
for k in range(1, N + 1):
    while True:
        if check(ans, k):
            break
        ans -= 1
    print(ans)
