def make_divisors(n: int) -> list:
    """自然数nの約数を列挙したリストを出力する
    計算量: O(sqrt(N))
    入出力例: 12 -> [1, 2, 3, 4, 6, 12]
    """
    divisors = []
    for k in range(1, int(n ** 0.5) + 1):
        if n % k == 0:
            divisors.append(k)
            if k != n // k:
                divisors.append(n // k)
    divisors = sorted(divisors)
    return divisors


def solve(val):
    res = []
    for i in range(n):
        tmp = a[i] % val
        if tmp == 0:
            continue
        res.append(a[i] % val)
    res = sorted(res)
    if not res:
        return True
    l_val = 0
    for i in range(len(res)):
        l_val += res[i]
        if l_val > k:
            l_pos = i - 1
            break
    else:
        return True
    r_val = 0
    for i in range(l_pos + 1, len(res)):
        r_val += val - res[i]
    return r_val <= k
            
      
        
    
n, k = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
div = make_divisors(sum_a)
ans = 0
for i in div:
    if solve(i):
        ans = max(ans, i)
print(ans)
