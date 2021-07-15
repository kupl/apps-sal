import itertools
def calc_cnt(nums,n):
    ans=1
    data=[str(i) for i in range(1,n+1)]
    for x in itertools.permutations(data):
        if " ".join(x)==nums:
            return ans
        ans+=1
    return ans

def main():
    n=int(input())
    p=input()
    q=input()
    p_cnt=calc_cnt(p,n)
    q_cnt=calc_cnt(q,n)
    ans=abs(p_cnt-q_cnt)
    print(ans)
def __starting_point():
    main()
__starting_point()
