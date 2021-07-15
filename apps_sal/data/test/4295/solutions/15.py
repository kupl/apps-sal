n, k =map(int,input().split())
ans1 = n%k
ans2 = k-ans1
print(min(ans1,ans2))
