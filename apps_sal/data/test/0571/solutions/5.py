import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
ans = []
count = 0
for i in s:
    if i == "(":
        ans.append(1)
    elif i == ")":
        ans.append(-1)
    else:
        ans.append(0)
        count += 1
x = sum(ans)
if abs(x) > count or x % 2 != count % 2:
    print(":(")
    return
hi = (x + count) // 2
mi = count - hi
for i in range(n):
    if ans[i] == 0 and mi:
        ans[i] = 1
        mi -= 1
    elif ans[i] == 0:
        ans[i] = -1
rui = [0] * (n + 1)
for i in range(n):
    rui[i + 1] = rui[i] + ans[i]
    if rui[i + 1] <= 0 and i != n - 1:
        print(":(")
        return
    if ans[i] == 1:
        ans[i] = "("
    else:
        ans[i] = ")"
print("".join(ans))
