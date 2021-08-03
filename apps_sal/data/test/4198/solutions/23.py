a, b, x = map(int, input().split())
max_ans = 10**9
min_ans = 0


def j(ans):
    nonlocal a
    nonlocal b
    return a * ans + b * len(str(ans))


if j(1) > x:
    print(0)
    return
if j(max_ans) <= x:
    print(max_ans)
    return

ans = (max_ans + min_ans) // 2

for i in range(40):
    if j(ans) > x:
        max_ans = ans
    elif j(ans) < x:
        min_ans = ans
    else:
        print(ans)
        return
    ans = (max_ans + min_ans) // 2

print(ans)
