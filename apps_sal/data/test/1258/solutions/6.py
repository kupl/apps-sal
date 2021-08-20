import sys
input = sys.stdin.readline
n = int(input())
adj_list = [[] for _ in range(n)]
for _ in range(n - 2):
    (q1, q2, q3) = map(int, input().split())
    adj_list[q1 - 1].append(q2 - 1)
    adj_list[q1 - 1].append(q3 - 1)
    adj_list[q2 - 1].append(q3 - 1)
    adj_list[q2 - 1].append(q1 - 1)
    adj_list[q3 - 1].append(q1 - 1)
    adj_list[q3 - 1].append(q2 - 1)
for i in range(n):
    adj_list[i] = list(set(adj_list[i]))
for i in range(n):
    if len(adj_list[i]) == 2:
        start = i
        break
ans = [start]
n1 = adj_list[start][0]
n2 = adj_list[start][1]
if len(adj_list[n1]) == 3:
    ans.append(n1)
else:
    ans.append(n2)
for i in range(2, n):
    n1 = ans[i - 2]
    n2 = ans[i - 1]
    s1 = set(adj_list[n1])
    s2 = set(adj_list[n2])
    s3 = s1 & s2
    if i >= 3:
        s3.remove(ans[i - 3])
    ans.append(list(s3)[0])
ans2 = [ai + 1 for ai in ans]
print(*ans2)
