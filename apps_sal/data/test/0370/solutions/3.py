def main():
    k=int(input())
    x,y=map(int,input().split())

    def calc(x,y,k):
        x_sign,y_sign,xy_swap=1,1,0
        if x<0:
            x_sign=-1
            x*=-1
        if y<0:
            y_sign=-1
            y*=-1
        if x<y:
            xy_swap=1
            x,y=y,x
        ans=[]
        d=x+y
        cnt=d//k
        #距離がkで割り切れるとき
        def pattern_0(x,y):
            x_now,y_now=0,0
            ans=[]
            cnt=(x+y)//k
            j=cnt
            for i in range(cnt):
                if x_now+k<x:
                    x_now+=k
                    ans.append([x_now,y_now])
                else:
                    y_now=k-x+x_now
                    x_now=x
                    ans.append([x_now,y_now])
                    j=i+1
                    break
            return ans+[[x,y_now+(i-j+1)*k] for i in range(j,cnt)]

        #cnt==0のとき
        #dが偶数のとき
        def pattern_1_even(x,y):
            return [[(x+y)//2,(x+y)//2-k],[x,y]]
        #dが奇数のとき
        def pattern_1_odd(x,y):
            if k%2==0:
                return -1
            return [[k,0]]+[[-i+k,j] for i,j in pattern_1_even(k-x,y)]

        #cnt>=1のとき
        #dが偶数のとき
        def pattern_2_even(x,y):
            cnt=(x+y)//k
            if k%2==0 or cnt%2==1:
                l=(k*(cnt+1)-(x+y))//2
            else:
                l=(k*(cnt+2)-(x+y))//2
            if cnt!=1:
                temp=[min(2*(k-l),x),max(2*(k-l)-x,0)]
                return [[k-l,-l],temp]+[[i+temp[0],j+temp[1]] for i,j in pattern_0(x-temp[0],y-temp[1])]
            else:
                return [[k-l,-l],[x,y]]
            
        #dが奇数のとき
        def pattern_2_odd(x,y):
            cnt=(x+y)//k
            if k%2==0:
                return -1
            else:
                if (x-k+y)<k:
                    if x-k<y:
                        return [[k,0]]+[[j+k,i] for i,j in pattern_1_even(y,x-k)]
                    else:
                        return [[k,0]]+[[i+k,j] for i,j in pattern_1_even(x-k,y)]
                if x-k<y:
                    return [[k,0]]+[[j+k,i] for i,j in pattern_2_even(y,x-k)]
                else:
                    return [[k,0]]+[[i+k,j] for i,j in pattern_2_even(x-k,y)]
        if d%k==0:
            temp=pattern_0(x,y)
        elif cnt==0:
            if d%2==0:
                temp=pattern_1_even(x,y)
            else:
                temp=pattern_1_odd(x,y)
        else:
            if d%2==0:
                temp=pattern_2_even(x,y)
            else:
                temp=pattern_2_odd(x,y)
        if temp==-1:
            return -1
        if xy_swap:
            temp=[[j*x_sign,i*y_sign] for i,j in temp]
        else:
            temp=[[i*x_sign,j*y_sign] for i,j in temp]
        return temp

    def out(x,y,k):
        temp=calc(x,y,k)
        if temp==-1:
            print(-1)
            return 0
        print(len(temp))
        for i in temp:
            print(*i)

    out(x,y,k)
main()
