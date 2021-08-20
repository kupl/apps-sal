n = int(input())
Ans = []
for j in range(n):
    Ans_0 = []
    s = input()
    len_s = len(s)
    s = list(s)
    for i in range(2, len_s):
        S = s[i - 2] + s[i - 1] + s[i]
        if i < len_s - 2:
            if S + s[i + 1] + s[i + 2] == 'twone':
                Ans_0.append(i + 1)
            elif S == 'one' or S == 'two':
                if Ans_0:
                    if Ans_0[-1] != i - 1:
                        Ans_0.append(i)
                else:
                    Ans_0.append(i)
        elif S == 'one' or S == 'two':
            if Ans_0:
                if Ans_0[-1] != i - 1:
                    Ans_0.append(i)
            else:
                Ans_0.append(i)
    Ans.append(Ans_0)
for i in range(len(Ans)):
    print(len(Ans[i]))
    print(*Ans[i])
