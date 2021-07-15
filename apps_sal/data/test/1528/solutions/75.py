n,x=map(int,input().split())
a=[1]#層の数 a[n]はレベルnのときの層の数
p=[1]#パテの数　p[n]はレベルnのときのパテの数
for i in range(n):
    a.append(2*a[-1]+3)
    p.append(a[-1]//2 +1)
#print(a,p)
def f(n,x):
    #print(n,x)
    if n==0:
        if x>=1:
            return 1
        else:
            return 0
    elif x==1:
        return 0
    elif x==a[n]:#レベルn全部取る場合
        return p[n]
    elif x==a[n-1]+2:#レベルnの真ん中まで取る場合
        return p[n-1]+1
    elif 1<x<a[n-1]+2:
        return f(n-1,x-1)#再帰関数。行列の2番目～真ん中の1個手前まで、つまりレベルn-1バーガーに移行。レベルnバーガーの最初は飛ばすので、xも-1する。
    else:
        return p[n-1]+1+f(n-1,x-a[n-1]-2)#再帰関数。行列真ん中の次～ラストの手前まで
print(f(n,x))
