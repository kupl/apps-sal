(N, K) = map(int, input().split())
D = list(map(int, input().split()))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = str(list(set(num) ^ set(D)))
ans = str(N)
clear = 0
while clear == 0:
    for i in range(len(ans)):
        if not ans[i] in num:
            break
        if i == len(ans) - 1:
            clear += 1
    ans = str(int(ans) + 1)
print(int(ans) - 1)
