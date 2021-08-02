n, q = map(int, input().split())
s = input()
l = [0] * n
tmp = 0
for i in range(n - 2, -1, -1):
    if s[i:i + 2] == "AC":
        tmp += 1
    l[i] += tmp
# print(l)
for i in range(q):
    L, R = map(int, input().split())
    print(l[L - 1] - l[R - 1])
