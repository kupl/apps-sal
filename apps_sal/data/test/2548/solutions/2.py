import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    a = [int(s[i]) - 1 for i in range(n)]
    data = [0] + a
    for i in range(1, n + 1):
        data[i] += data[i - 1]
    dic = {}
    for i in range(n + 1):
        if data[i] not in dic:
            dic[data[i]] = 0
        dic[data[i]] += 1
    ans = 0
    for d in dic:
        ans += dic[d] * (dic[d] - 1) // 2
    print(ans)
