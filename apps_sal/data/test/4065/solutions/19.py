n = int(input())
a = list(map(int, input().split()))
a.append(a[n - 1] * 3)
max_ans = 1
ans = 1
for i in range(n):
    if a[i] * 2 < a[i + 1]:
        if ans > max_ans:
            max_ans = ans
        ans = 1
    else:
        ans += 1
print(max_ans)
