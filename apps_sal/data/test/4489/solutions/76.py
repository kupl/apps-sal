N = int(input())
s = []
for i in range(N):
    s.append(input())

M = int(input())
t = []
for i in range(M):
    t.append(input())

money_list = []
for i in range(N):
    money = s.count(s[i]) - t.count(s[i])
    money_list.append(money)

ans = max(money_list)
if ans < 0:
    print("0")
else:
    print(ans)
