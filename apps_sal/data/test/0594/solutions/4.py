n, m = list(map(int, input().split()))
right = sorted(list(map(int, input().split())))
wrong = sorted(list(map(int, input().split())))
ans = max(right[0] * 2, right[-1])
if ans < wrong[0]:
    print(ans)
else:
    print(-1)

