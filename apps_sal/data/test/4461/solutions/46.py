import sys
h, w = list(map(int, input().split()))
if h%3==0 or w%3==0:
    print((0))
    return
ans=h*w #inf
for i in range(1, h):
    s1=i*w
    s2=(h-i)*(w//2)
    s3=h*w-s1-s2
    now=max(s1, s2, s3)-min(s1, s2, s3)
    #print(i, now)
    ans=min(ans, now)
for j in range(1, w):
    s1=h*j
    s2=(w-j)*(h//2)
    s3=h*w-s1-s2
    now=max(s1, s2, s3)-min(s1, s2, s3)
    ans=min(ans, now)
if w>3:
    ans=min(ans, h)
if h>3:
    ans=min(ans, w)
print(ans)

