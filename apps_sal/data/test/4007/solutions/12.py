n = int(input())
a = list(map(int, input().split()))
send = []
recv = []
vis = [0] * n
for i in range(n):
    if a[i] == 0:
        send.append(i + 1)
    else:
        vis[a[i] - 1] = 1
for i in range(n):
    if vis[i] == 0:
        recv.append(i + 1)
send.sort()
recv.sort()
recv = list(set(send) & set(recv)) + list(set(recv) - set(send))
p = 0
for i in range(len(send)):
    while recv[p] == -1:
        p = (p + 1) % len(recv)
    if send[i] == recv[p]:
        p = (p + 1) % len(recv)
        while recv[p] == -1:
            p = (p + 1) % len(recv)
    a[send[i] - 1] = recv[p]
    recv[p] = -1
    p = (p + 1) % len(recv)
print(*a)
