n = int(input())
a = list(map(int, input().split()))
ans_h = {}
ans = []
for (i, ele) in enumerate(a):
    ans_h[ele] = i + 1
for i in range(1, n + 1):
    ans.append(str(ans_h[i]))
print(' '.join(ans))
