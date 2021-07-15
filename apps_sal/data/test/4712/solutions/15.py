H,W=list(map(int,input().split()))
a=[input() for _ in range(H)]
for i in range(0,H):
    a[i]='#'+a[i]+'#'

print(('#'*(W+2)))
for i in range(H):
    print((a[i]))
print(('#'*(W+2)))

