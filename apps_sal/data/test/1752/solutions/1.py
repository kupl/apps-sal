n = int(input())
a = sorted(list(map(int, input().split())))

answer_left = []
ansewr_right = []
for i in range(0, n - 1, 2):
    answer_left.append(a[i])
    ansewr_right.append(a[i + 1])

if len(ansewr_right) + len(answer_left) < n:
    answer_left.append(a[-1])

print(*answer_left, *ansewr_right[::-1])
