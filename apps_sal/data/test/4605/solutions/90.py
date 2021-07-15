n,a,b = map(int, input().split())

ans = 0
for num in range(n+1):
    str_num = str(num)
    num_list = list(str_num)
    total = sum([int(i) for i in num_list])
    if total >= a and total <= b:
        ans+=num
print(ans)
