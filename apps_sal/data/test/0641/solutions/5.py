3

mnthnums = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def of_month(n):
    ans = 0
    for i in range(12):
        if mnthnums[i] >= n:
            ans += 1
    return ans


def of_week(n):
    if n >= 5:
        n -= 4
    else:
        n += 2
    return (366 - n + 7) // 7


strs = input().split()
n = int(strs[0])

if strs[-1] == "week":
    print(of_week(n))
else:
    print(of_month(n))

