#n = int(input())
n, q = list(map(int, input().split()))
#bl = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
s = input()
acnum = [0]*(n+1)
for i in range(2, n+1):
    if s[i-2:i] == 'AC':
        acnum[i] += acnum[i-1]+1
    else:
        acnum[i] += acnum[i-1]

for i in range(q):
    l, r = list(map(int, input().split()))
    print((acnum[r]-acnum[l]))

