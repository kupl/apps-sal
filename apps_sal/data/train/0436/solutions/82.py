class Solution:
    def minDays(self, n: int) -> int:
        def fun(n,d):
            if(n<=1):
                return n
            if(n in d):
                return d[n]
            d[n]=min(n%2+fun(n//2,d),n%3+fun((n)//3,d))+1
            return d[n]
            # t=0
            # if(n%3==0):
            #     b=fun(n-2*n//3,d)+1
            #     t=1
            # elif(n%3==1):
            #     b=fun((n-1)-2*(n-1)//3,d)+2
            #     #b=float(\"inf\")
            #     n=n-1
            #     t=1
            # else:
            #     b=float(\"inf\")
            # #v=fun(n-1,d)+1
            # if(t==0):
            #     if(n%2==0):
            #         a=fun(n//2,d)+1
            #     elif(n%2==1):
            #         a=fun((n-1)-(n-1)//2,d)+2
            #         n=n-1
            # else:
            #     a=float(\"inf\")
            # #if(v1==v2):
            # #      d[v1]=min(a,b)
            # d[n]=min(a,b)
            # return d[n]
        d={}
        return fun(n,d)
