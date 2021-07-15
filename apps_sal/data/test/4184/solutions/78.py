def ans129(N:int, W:str):
    W_list=list(map(int,W.split()))
    ans_count=100
    for i in range(N):
        if abs(sum(W_list[:i])-sum(W_list[i:]))<ans_count:
            ans_count=abs(sum(W_list[:i])-sum(W_list[i:]))
    return ans_count

def __starting_point():
    N=int(input())
    W=input()
    print(ans129(N,W))
__starting_point()
