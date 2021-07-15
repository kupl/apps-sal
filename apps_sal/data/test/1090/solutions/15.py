n, k = map(int, input().split())
S = input()
h = 0
for i in range(1,n):
    if S[i]==S[i-1]:
        h += 1
print(min(h+2*k, n-1))
