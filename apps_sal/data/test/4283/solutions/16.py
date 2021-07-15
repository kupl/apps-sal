n = int(input())
A = list(map(int, input().split()))


A.sort()

ans = 0

cur_min_idx = 0
cur_students = 1

idx = 1
while idx < n:
    if A[idx] - A[cur_min_idx] <= 5:
        cur_students += 1
        idx += 1
    else:
        cur_min_idx += 1
        cur_students -= 1

    ans = max(ans, cur_students)

ans = max(ans, cur_students)

print(ans)
