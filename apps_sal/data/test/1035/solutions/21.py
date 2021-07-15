def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

A, B = list(map(int, input().split()))

A_yakusu = make_divisors(A)
B_yakusu = make_divisors(B)
yakusu_set = set(A_yakusu) & set(B_yakusu)
yakusu_list = list(yakusu_set)
 
if max(yakusu_list) != 1:
    print((len(factorization(max(yakusu_list)))+1)) 
else:
    print((1))

