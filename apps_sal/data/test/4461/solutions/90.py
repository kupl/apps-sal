from sys import stdin
def main():
    #入力
    readline=stdin.readline
    h,w=map(int,readline().split())

    if h*w%3==0:
        ans=0
    else:
        ans=float("inf")
        #縦方向に全探索
        s1=w//2*h
        s2=h*w-s1
        for i in range(1,h):
            s3=i*w
            s1-=w//2
            s2-=w-w//2
            ans=min(ans,max(s1,s2,s3)-min(s1,s2,s3))

        for i in range(1,h-1):
            s3=i*w
            s1=(h-i)//2*w
            s2=h*w-s3-s1
            ans=min(ans,max(s1,s2,s3)-min(s1,s2,s3))

        #横方向に全探索
        s1=h//2*w
        s2=h*w-s1
        for j in range(1,w):
            s3=j*h
            s1-=h//2
            s2-=h-h//2
            ans=min(ans,max(s1,s2,s3)-min(s1,s2,s3))
        
        for j in range(1,w-1):
            s3=j*h
            s1=(w-j)//2*h
            s2=h*w-s3-s1
            ans=min(ans,max(s1,s2,s3)-min(s1,s2,s3))

    print(ans)

def __starting_point():
    main()
__starting_point()
