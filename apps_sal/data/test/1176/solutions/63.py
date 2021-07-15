n = int(input())
a = list(map(int, input().split()))
mini = 10**9 + 1
s = 0
flag = 1
for i in a:
    mini = min(mini, abs(i))
    if i < 0:
        flag *= -1
    s += abs(i)
if flag == 1:
    print(s)
else :
    print(s-2*mini)
