MOD = 10**9+7
def resolve():
    N = int(input())
    A = list(map(lambda x: bin(int(x))[2:].zfill(60), input().split()))
    ans = 0
    for i in range(60):
        one_cnt = 0
        zero_cnt = 0
        for a in A:
            if a[i] == "1":
                one_cnt += 1
            else:
                zero_cnt += 1
        ans += (one_cnt*zero_cnt)*(2**(59-i))
        ans %= MOD
    print(ans)

    

if '__main__' == __name__:
    resolve()
