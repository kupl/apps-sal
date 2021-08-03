n = int(input())
a = list(map(int, input().split()))
ans_list = [0] * n
for i in range(n):
    ans_list[a[i] - 1] = (i + 1)
ans = ""
for i in range(n):
    ans += str(ans_list[i])
    ans += " "
print(ans)
