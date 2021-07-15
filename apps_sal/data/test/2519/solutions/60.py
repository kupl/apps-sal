n, k = map(int, input().split())
p = list(map(int, input().split()))
e = []

for i in range(n):
    e.append(p[i] + 1)

sum_e = [0]

for i in range(1,n+1):
    sum_e.append(sum_e[i-1]+e[i-1])

ans = []

for i in range(n-k+1):
    ans.append(sum_e[i+k]-sum_e[i])

print(max(ans)/2)
