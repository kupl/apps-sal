s = input()
n = len(s)
K = int(input())
ans = []
an = set()
for i in range(1,min(5,n)+1):
    for j in range(n-i+1):
        S = s[j:j+i]
        if S not in an:
            ans.append(S)
            an.add(S)
ans.sort()
print(ans[K-1])
