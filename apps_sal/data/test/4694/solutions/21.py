N=int(input())
a=str(input())

def ans064(N:int, a:str):
    a_list=sorted(map(int,a.split()))
    return(a_list[-1]-a_list[0])

print(ans064(N,a))
