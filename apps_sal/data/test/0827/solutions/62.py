N = int(input())
T = str(input())
S = str()
cnt = 0
p = 0
q = 0
for i in range(N):
    S = S + '110'
for i in range(3):
    if S[i:N + i] == T:
        p = i
        q = i + N - 1
        cnt = cnt + 1
        break
z = q // 3 + 1
if cnt == 0:
    print(0)
elif T == '1':
    print(2 * 10 ** 10)
else:
    print(10 ** 10 - (z - 1))
