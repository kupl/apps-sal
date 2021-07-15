n = int(input())
m = 10**9 +7

x = 10**n % m
y = 9**n % m
z = 8**n % m

print((x - y*2 + z)% m)
