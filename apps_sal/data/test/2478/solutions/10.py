N = int(input())
motoS = input()
S = list(motoS)
start = 0
end = 0
for i in range(N):
    if S[i] == '(':
        end += 1
    else:
        end -= 1
    if end < 0:
        start += 1
        end = 0
print('(' * start + motoS + ')' * end)
