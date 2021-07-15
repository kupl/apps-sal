def get_divisor(num, max_val):
    ret = []
    num_sq = int(num**0.5)
    for k in range(1, num_sq+1):
        if num % k == 0:
            if k <= max_val: ret.append(k)
            if num//k <= max_val: ret.append(num//k)
            
    return ret

# 下からmodが低いのを取ってきてマッチングを取る
def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    max_A = max(A)
    div = get_divisor(sum_A, max_A+K)
    ret = 1
    for d in div:
        sum_k = 0
        red_k = 0
        flag = True
        mod_d = [a%d for a in A]
        mod_d.sort()
        # print(d, mod_d)
        for a in mod_d:
            if sum_k+a <= K:
                sum_k += a
            else: 
                red_k += d-a
            if sum_k-red_k < 0:
                break

        if (sum_k-red_k)%d == 0: ret = max(ret, d)
            
    print(ret)
    
solve()
