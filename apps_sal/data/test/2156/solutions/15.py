n = int(input())
l = list(map(int, input().split()))
pre = [0]
for i in l:
    pre.append(pre[-1] + i)
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print((pre[r] - pre[l - 1]) // 10)
