MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    
    cum = [0] * (n + 1)
    dic = {0:1}
    ans = 0
    for i in range(min(n,k - 1)):
        cum[i + 1] = (cum[i] + a[i])%k
        tmp = (cum[i + 1] - i - 1)%k
        if tmp in dic:
            dic[tmp] += 1
        else:
            dic[tmp] = 1

    for v in list(dic.values()):
        ans += v * (v - 1)//2


    for i in range(max(n - k + 1,0)):
        dic[(cum[i] - i)%k] -= 1
        cum[i + k] = (cum[i + k - 1] + a[i + k - 1])%k
        tmp = (cum[i + k] - i - k)%k
        if tmp in dic:
            ans += dic[tmp]
            dic[tmp] += 1
        else:
            dic[tmp] = 1

    print(ans)
def __starting_point():
    main()   

__starting_point()
