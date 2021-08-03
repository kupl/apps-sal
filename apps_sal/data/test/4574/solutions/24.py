N = int(input())
A = list(map(int, input().split()))

count = {}
rect = {}
for i in range(N):
    if A[i] in rect:
        rect[A[i]] += 1
    elif A[i] in count:
        rect[A[i]] = 2
    else:
        count[A[i]] = 1

if len(rect) < 1:
    ans = 0
else:
    x = max(rect)
    if rect[x] >= 4:
        ans = x * x
    else:
        del rect[x]
        if len(rect) < 1:
            ans = 0
        else:
            y = max(rect)
            ans = x * y
print(ans)
