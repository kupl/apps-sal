#a,b,c,d = map(int, input().split())
n = int(input())
ans = (10**n - 9**n * 2 + 8**n) % 1000000007
print(ans)
