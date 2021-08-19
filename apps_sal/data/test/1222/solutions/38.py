import queue
k = int(input())
que = queue.Queue()
for i in range(1, 10):
    que.put(i)
for i in range(1, k + 1):
    ans = que.get()
    keta1 = ans % 10
    if keta1 == 0:
        append_list = [ans * 10, ans * 10 + 1]
    elif keta1 == 9:
        append_list = [ans * 10 + 8, ans * 10 + 9]
    else:
        append_list = [ans * 10 + keta1 - 1, ans * 10 + keta1, ans * 10 + keta1 + 1]
    for item in append_list:
        que.put(item)
print(ans)
