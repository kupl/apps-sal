import queue
(n, m) = list(map(int, input().split()))
dic = {}
count = 0
q = queue.Queue()
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    if not a - 1 in dic:
        dic[a - 1] = [b - 1]
    else:
        dic[a - 1].append(b - 1)
    if not b - 1 in dic:
        dic[b - 1] = [a - 1]
    else:
        dic[b - 1].append(a - 1)
dp = [0] * n
for i in range(n):
    if dp[i] == 0:
        count += 1
        dp[i] = count
        if i in dic:
            for j in dic[i]:
                dp[j] = count
                q.put(j)
        while not q.empty():
            temp = q.get()
            if temp in dic:
                for j in dic[temp]:
                    if dp[j] == 0:
                        dp[j] = count
                        q.put(j)
print(count)
