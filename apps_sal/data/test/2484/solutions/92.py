def ind(S):
    L4 = list()
    for i in range(len(S)):
        if S[len(S) - i - 1] == "1":
            L4.append(i)
    return set(L4)


N = int(input())
L = list(map(int, input().split()))
L = [ind(bin(i)[2:]) for i in L]
ans = 0
n = 0
i = 0
T = set()
while True:
    if i == N and n == N:
        break
    elif i == N:
        ans += i - n
        n += 1
        continue
    if T & L[i] == set():
        T = T | L[i]
        ans += 1
        i += 1
    else:
        T = T - L[n]
        n += 1
        ans += i - n
    if i == N and n != N:
        n += 1
print(ans)
