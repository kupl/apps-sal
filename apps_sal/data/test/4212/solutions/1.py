import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m,q = LI()
    require = [LI() for _ in range(q)]
    itr = itertools.combinations_with_replacement(list(range(1,n+2)),m-1)     
    ans = 0
    for i in itr:
        lst = [0 for _ in range(n+2)]
        lst[0] = 1
        cnt = 0
        for j in i:
            lst[j] += 1
        lst = list(itertools.accumulate(lst))
        for re in require:
            if lst[re[1]]-lst[re[0]]==re[2]:
                cnt += re[3]
        ans = max(cnt,ans)
    print(ans)

main()
