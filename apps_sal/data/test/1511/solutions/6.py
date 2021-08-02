N, M, k = list(map(int, input().split()))
cash = [-1] * (k + 1)
cash_lock = [False] * (k + 1)
processers = [0] * (N)
process = []
for i in range(N):
    process.append(list(map(int, input().split())))
for j in range(M):
    for i in range(N):
        if processers[i] == 0:
            if process[i][j] != 0:
                cash_num = process[i][j]
                if cash[cash_num] == -1 and not cash_lock[cash_num]:
                    cash[cash_num] = i
                elif cash_lock[cash_num]:
                    processers[i] = j + 1
                elif cash[cash_num] != -1:
                    processers[i] = j + 1
                    processers[cash[cash_num]] = j + 1
                    cash_lock[cash_num] = True
    for i in range(1, k + 1):
        cash[i] = -1
for i in range(N):
    print(processers[i])
