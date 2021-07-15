N, K = list(map(int,input().split()))
S = input()

capital = ['A','B','C']
small = ['a','b','c']

i = capital.index(S[K-1])
ans = S[:K-1]+small[i]+S[K:]
print(ans)

