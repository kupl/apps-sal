n, m = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = []
for i in range(n):
    if sum(t[:i+1]) <= m:
        ans.append(0)
    else:
        remain = sum(t[:i+1]) - m
        fail_student = sorted(t[:i], reverse = True)
        for j in range(i):
            remain -= fail_student[j]
            if remain <= 0:
                ans.append(j+1)
                break
print(" ".join(map(str, ans)))

