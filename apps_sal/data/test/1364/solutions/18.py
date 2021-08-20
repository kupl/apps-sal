N = int(input())
A = list(map(int, input().split()))
ans = 0
prev = A[0]
prev_num = 0
tmp = 0
for a in A:
    if a == prev:
        tmp += 1
    else:
        prev_num = tmp
        tmp = 1
    ans = max(ans, min(tmp, prev_num))
    prev = a
print(ans * 2)
