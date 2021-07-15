n, q = map(int, input().split())
S = input()
flag = False
L = [0 for _ in range(n)]
cnt = 0
for i, s in enumerate(S):
    if flag:
        if s == "C":
            cnt += 1
        flag = False
    if s == "A":
        flag = True
    L[i] = cnt

for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(L[r] - L[l])
