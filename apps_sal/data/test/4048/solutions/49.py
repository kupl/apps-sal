n = int(input())
ans = float('inf')

for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        j = n//i
        ans = min(ans, i-1+j-1)

print(ans)
