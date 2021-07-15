n = int(input())
s = input()
S = [ord(znak) - 97 for znak in s]
a = list(map(int, input().strip().split(' ')))
#print(n, S, a)

MOD = 10**9 + 7

st = [0]*(n+1)
st[0] = 1
maks = [0]*(n+1)
minway = [10**4]*(n+1)
minway[0] = 0
for i in range(1, n + 1):
    cnt = 0
    maks_dolzina = n
    for j in range(i, 0, -1):
        maks_dolzina = min(maks_dolzina, a[S[j - 1]])
        if i - j + 1 > maks_dolzina:
            break
        cnt += st[j-1]
        maks[i] = max(i-j+1, maks[j-1], maks[i])
        minway[i] = min(minway[i], 1 + minway[j-1])
    st[i] = cnt

print(st[-1] % MOD)
print(maks[-1])
print(minway[-1])


