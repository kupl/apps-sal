n = int(input())
arr = list(map(int, input().split()))
arr.sort()
n = n // 2
s_1 = 0
s_2 = 0
nech = 1
chet = 2
for i in range(n):
    s_1 = s_1 + abs(nech - arr[i])
    nech += 2
    s_2 = s_2 + abs(chet - arr[i])
    chet +=2
print(min(s_1,s_2))
