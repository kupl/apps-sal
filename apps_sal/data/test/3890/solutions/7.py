inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])
print(k**(k-1)*(n-k)**(n-k) % 1000000007)
