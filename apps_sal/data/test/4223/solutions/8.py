N = int(input())
S = list(input())

# N=O(10^5)なのでO(N)で解く
# 同じ文字を1つのグループと見るときに、何グループできるか？
# 文字が変化する点に着目すればよい。するとグループ数は（変化点+1）個と求まる！

ans=1
for i in range(N-1):
  if S[i] != S[i+1]: ans += 1

print(ans)
