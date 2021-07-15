def calc_factors(N):
    """
    約数をlistでreturn
    この問題はK>1なので、約数に1を含めてない
    """
    i=2
    factors={N}
    while i*i<=N:
        if N%i==0:
            factors.add(i)
            factors.add(N//i)
        i+=1
    return list(sorted(factors))


N = int(input())


if N==2:
    print((1))
    return
#割り算しない場合
ans = len(calc_factors(N-1))
#割り算する場合
for fac in calc_factors(N):
    tmp=N
    while tmp%fac==0:
        tmp//=fac
    if tmp%fac==1:
        ans+=1
print(ans)

