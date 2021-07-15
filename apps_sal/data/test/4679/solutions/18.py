a=[input(),input(),input()]
now=0
while a[now]:
    y=a[now][0];a[now]=a[now][1:];now=ord(y)-ord('a')
print("ABC"[now])
