n = int(input())
k = int(input())
x_list = list(map(int, input().split()))
ans = 0
for i in x_list:
    if 2*i < k:
        ans += 2*i
    else :
        ans += (k-i)*2
print(ans)

