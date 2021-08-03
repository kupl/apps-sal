def digitSum(k):
    if k == 0:
        return 0
    else:
        return digitSum(k // 10) + k % 10


N = int(input())
if N % digitSum(N) == 0:
    print("Yes")
else:
    print("No")
