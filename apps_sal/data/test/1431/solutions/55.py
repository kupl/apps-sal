N = int(input())
Alist = list(map(int, input().split()))
Answer = [0] * (N + 1)
M = 0
for i in range(1, len(Alist) + 1):
    A = Alist[-i]
    n = N + 1 - i
    if sum(Answer[n::n]) % 2 != A:
        Answer[-i] = 1
        M += 1
print(M)
Ans = []
for k in range(len(Answer)):
    if Answer[k] == 1:
        Ans.append(k)
print(*Ans[0:], end='\t')
