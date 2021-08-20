S = str(input())
for i in range(1, int(len(S) / 2)):
    T = S[0:len(S) - 2 * i]
    clear = 0
    m = int(len(T) / 2)
    for j in range(m):
        if T[j] == T[m + j]:
            clear += 1
    if clear == m:
        print(len(T))
        break
