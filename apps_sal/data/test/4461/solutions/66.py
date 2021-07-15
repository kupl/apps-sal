h,w=list(map(int,input().split()))

def sds(h,w):
    sdmin=h*w
    for hi in range(1,h):
        s1=hi*w
        s2=(h-hi)*(w//2)
        s3=(h-hi)*(w-w//2)
        sd=max(s1,s2,s3)-min(s1,s2,s3)
        sdmin=min(sdmin,sd)
    
        h2=(h-hi)//2
        s2=h2*w
        s3=(h-hi-h2)*w
        sd=max(s1,s2,s3)-min(s1,s2,s3)
        sdmin=min(sdmin,sd)

    return sdmin

print((min(sds(h,w),sds(w,h))))

