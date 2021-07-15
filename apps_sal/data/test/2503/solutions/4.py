from subprocess import*
call(('julia','-e',"""
const lines=readlines()
input()=shift!(lines)
int(s)=parse(Int32,s)
intLine()=map(int,split(input()))
function nextLine(k)
    x,y,c=split(input())
    int(x)%2k+1,(int(y)+(c=="W")k)%2k+1
end
function solve(k,g)
    m=0
    for i=1:2k,j=1:2k
        a=0
        for x=-1:2,y=-1:2
            (x+y)%2!=0&&continue
            v,w=i+x*k,j+y*k
            v>0<w&&(a+=g[min(2k,v)][min(2k,w)])
            v>k&&w>0&&(a-=g[min(2k,v-k)][min(2k,w)])
            w>k&&v>0&&(a-=g[min(2k,v)][min(2k,w-k)])
            v>k<w&&(a+=g[min(2k,v-k)][min(2k,w-k)])
        end
        m=max(m,a)
    end
    m
end
function main()
    n,k=intLine()
    g=Array{Int32,1}[[0for j=1:2k]for i=1:2k]
    for i=1:n
        x,y=nextLine(k)
        g[x][y]+=1
    end
    println(solve(k,cumsum(map(cumsum,g))))
end
main()
"""))
