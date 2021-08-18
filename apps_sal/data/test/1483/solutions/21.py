from sys import stdin, stdout


def rint():
    return map(int, stdin.readline().split())


n = int(input())
p = list(rint())
p = [0] + p

ans = []
for i in range(1, n + 1):
    cnt = [0] * (n + 1)
    a = i
    cnt[a] += 1
    while True:
        if cnt[a] == 2:
            ans.append(a)
            break
        cnt[p[a]] += 1
        a = p[a]

print(*ans)
