n, a, b = list(map(int, input().split()))
a_list = input().split()
b_list = input().split()
ans = ["-1"] * n
for i in range(n):
    if a_list.count(str(i + 1)):
        ans[i] = "1"
    else:
        ans[i] = "2"
print(" ".join(ans))
