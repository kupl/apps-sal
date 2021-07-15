def expect(n):
        return (n+1)/2

nk = input().split()
N = int(nk[0])
K = int(nk[1])
p = input().split()

tmp = 0
for i in range (K):
    tmp += expect(int(p[i]))

tmpMax = tmp

for i in range(N - K):
    tmp -= expect(int(p[i]))
    tmp += expect(int(p[i+K]))
    tmpMax = max(tmpMax, tmp)

print(tmpMax)


