count = {}
ans = []


def mx(a, b, c):
    ans.append((a, b, c))
    count[a] -= 1
    count[b] -= 1
    count[c] -= 1


n = int(input())
nums = list(map(int, input().split()))
if 5 in nums or 7 in nums or nums.count(1) != n // 3:
    print(-1)
else:
    for i in [1, 2, 3, 4, 6]:
        count[i] = nums.count(i)
    while count[2] > 0 and count[4] > 0:
        mx(1, 2, 4)
    while count[2] > 0 and count[6] > 0:
        mx(1, 2, 6)
    while count[3] > 0 and count[6] > 0:
        mx(1, 3, 6)
if sum(count.values()) > 0:
    print(-1)
else:
    for (a, b, c) in ans:
        print(a, b, c)
