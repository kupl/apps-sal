N = int(input())
T = str(input()); S = str(); cnt = 0; p = 0; q = 0

for i in range(N):
    S = S + "110"
# print(S)
for i in range(3):
    # print(i,S[i:N+i],T)
    if S[i:N + i] == T:
        p = i
        q = i + N - 1
        cnt = cnt + 1
        # print("p",i)
        break
z = q // 3 + 1

# print(z)
# print(cnt)

if cnt == 0:
    print(0)
else:
    if T == "1":
        print(2 * 10**10)
    else:
        print(10**10 - (z - 1))
