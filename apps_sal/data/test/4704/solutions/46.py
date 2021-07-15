N = int(input())
lsa = list(map(int,input().split()))
sunu = lsa[0]
ara = sum(lsa)- lsa[0]
ans = abs(ara-sunu)
for i in range(1,N-1):
    sunu += lsa[i]
    ara -= lsa[i]
    ans = min(ans,abs(ara-sunu))
print(ans)
