import sys
input = sys.stdin.readline


n = int(input())
s = input()

ans = [0] * (n + 1)
for i in range(n):
    if s[i] == "(":
        ans[i + 1] += ans[i] + 1 
    else:
        ans[i + 1] += ans[i] - 1 

if ans[-1] != 0:
    print(-1)
    return

res = 0
flag = False
for i in range(n + 1):
    if ans[i] == -1 and not flag:
        ind = i
        flag = True
    elif ans[i] == 0 and flag:
        res += i - ind + 1
        flag = False
print(res)
