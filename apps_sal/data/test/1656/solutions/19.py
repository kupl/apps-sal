s = input()
ans = 0
arr = s.split('o')
wsall = 0
for i in arr:
    if len(i)>1:
        wsall+=len(i)-1
ws=0
for i in range(len(arr)-1):
    if len(arr[i])>1:
        ws+=len(arr[i])-1
        wsall-=(len(arr[i])-1)
    ans += ws * wsall
print(ans)




