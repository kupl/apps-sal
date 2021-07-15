S_list = list(map(int,input().split()))
a,b,c = S_list
bell = int(b/a)
if bell >= c:
    result = c
else:
    result = bell
print(result)
