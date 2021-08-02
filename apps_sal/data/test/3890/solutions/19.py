a = list(map(int, input().split()))
n = a[0]
k = a[1]
rem = n - k
pans = (rem**rem) % 1000000007
rem1 = n - rem - 1
pans1 = ((rem1 + 1)**rem1) % 1000000007
ans = (pans * pans1) % 1000000007
print(ans)
