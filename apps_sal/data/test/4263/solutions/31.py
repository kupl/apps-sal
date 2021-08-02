S = input()
l = len(S)
answer = 0
for i in range(l):
    for j in reversed(range(i + 1, l + 1)):
        T = S[i:j]
        T_1 = T.replace('A', '').replace('C', '').replace('G', '').replace('T', '')
        if len(T_1) == 0:
            pri = j - i
            if pri > answer:
                answer = pri
print(answer)
