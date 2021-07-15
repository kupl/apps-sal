n = int(input())
a_list = list(map(int, input().split()))

sum = 0
s_list=[]
ans = 0

for i in range(n):
    sum += a_list[i]
    s_list.append(sum)

for i in range(n-1):
    ans += a_list[i] * (s_list[n-1]-s_list[i])

print((ans % (7+10**9)))

