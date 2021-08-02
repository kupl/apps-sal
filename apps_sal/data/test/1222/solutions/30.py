from collections import deque


def main():
    K = int(input())
    q = deque()
    for i in range(1, 10, 1):
        q.append(i)
    list = []
    while (len(list) <= 100002):
        v = q.popleft()
        list.append(v)
        amari = v % 10
        if amari != 0 and amari != 9:
            q.append((v * 10) + amari - 1)
            q.append((v * 10) + amari)
            q.append((v * 10) + amari + 1)
        elif amari == 0:
            q.append((v * 10) + amari)
            q.append((v * 10) + amari + 1)
        else:
            q.append((v * 10) + amari - 1)
            q.append((v * 10) + amari)

    return list[K - 1]


print((main()))
