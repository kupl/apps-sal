n = int(input())
a = list(map(int, input().split()))
ans_1 = 0
ans_2 = 0
for i in range(n):
    if a[i] % 2 == 0:
        ans_1 += 1
    else:
        ans_2 += 1

print(min(ans_1, ans_2))
