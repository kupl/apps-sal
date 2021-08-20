N = int(input())
A = list(map(int, input().split()))
num = [0] * (2 * 10 ** 5)
ans = 0
for i in A:
    num[i - 1] += 1
for j in range(2 * 10 ** 5):
    ans += num[j] * (num[j] - 1) // 2
for p in A:
    print(ans - num[p - 1] + 1)
