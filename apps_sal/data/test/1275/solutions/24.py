from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, k = nii()

ans = 0
for i in range(2, 2 * n + 1):
    j = i - k

    if not 2 <= j <= 2 * n:
        continue

    num1 = 2 * min(i - 1, n) - i + 1
    num2 = 2 * min(j - 1, n) - j + 1

    ans += num1 * num2

print(ans)
