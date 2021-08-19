"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc077/tasks/arc077_c

お気に入りを決めてる時、その数字を超えるような移動が発生した場合だけ、ボタン2が有効になる。
ALLボタン１に比べて、何回節約できるかをimos法で計算する

"""
(n, m) = map(int, input().split())
lis = [0] * m
state = [0] * n
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
start = [[] for i in range(m)]
end = [[] for i in range(m)]
allsum = 0
for i in range(n - 1):
    allsum += (a[i + 1] - a[i]) % m
    if a[i + 1] == (a[i] + 1) % m:
        continue
    start[(a[i] + 1) % m].append(i)
    end[a[i + 1] % m].append(i)
imosnum = 0
plus = 0
for i in range(2 * m):
    plus += imosnum
    lis[i % m] += plus
    for j in end[i % m]:
        if state[j] == 1:
            plus -= (a[j + 1] - (a[j] + 1)) % m
            state[j] = 2
            imosnum -= 1
    for j in start[i % m]:
        if state[j] == 0:
            imosnum += 1
            state[j] = 1
if allsum - max(lis) < 0:
    print(asxacscd)
print(allsum - max(lis))
