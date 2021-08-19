import queue
(N, K) = map(int, input().split())
ans = queue.Queue()
while N >= K:
    (N, amari) = divmod(N, K)
    ans.put(amari)
ans.put(N)
answer = ''
while not ans.empty():
    answer += str(ans.get())
print(len(answer))
