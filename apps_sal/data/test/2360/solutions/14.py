
t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    L = []
    R = []
    for _ in range(n):
        l, r = list(map(int, input().split()))
        L.append(l)
        R.append(r)
    time = [0 for _ in range(n)]
    flag = [0 for _ in range(n)]
    for i in range(1, max(R) + 1):
        for j in range(n):
            if L[j] == i:
                flag[j] = 1
        for j in range(n):
            if flag[j] == 1:
                flag[j] = 0
                time[j] = i
                break
        for j in range(n):
            if flag[j] == 1 and R[j] == i:
                flag[j] = 0
    ans.append(time)

for i in range(t):
    answer = list(map(str, ans[i]))
    print(" ".join(answer))
