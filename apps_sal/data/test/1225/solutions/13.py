h=int(input())
def fh(x):
    if x==1:
        return 1
    else:
        return 2*fh(x//2)+1
ans=fh(h)
print(ans)
