n,a,b,k = list(map(int,input().split()))

s = input()

sm = 0
num = 0
res = []
for i in range(n):
    if s[i] == "1":
        sm = 0
    if s[i] == "0":
        sm += 1
        if sm == b:
            num += 1
            res.append(i+1)
            sm = 0
k = num - a + 1
print(k)
print(*res[:k])

