(n, q) = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]
cnt = 0
lst = []
for i in range(n):
    if s[i - 1:i + 1] == 'AC':
        cnt += 1
    lst.append(cnt)
for i in range(q):
    print(lst[lr[i][1] - 1] - lst[lr[i][0] - 1])
