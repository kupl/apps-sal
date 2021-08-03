# IAWT
a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
     31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def starting(x):  # x is index
    if x + n - 1 >= len(a):
        return False
    for i in range(n):
        if s[i] != a[i + x]:
            return False
    return True


n = int(input())
s = list(map(int, input().split()))
ans = "No"
for i in range(len(a)):
    if starting(i):
        ans = "Yes"

print(ans)
