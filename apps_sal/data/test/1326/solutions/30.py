
"""
def factorization(n):
    if (n == 1 ):
        return [1]
    arr = []
    temp = n

    
    for i in range(2, int(-(-n**0.5//1))+1) :
        if ( temp % i == 0):
            cnt = 0
            while (temp % i == 0):
                cnt +=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
    return [arr[1]+1 for arr in arr ]


sum_ans = 0
def cal(list):
    ans = 1
    for i in list:
        ans *= i

    return ans


for i in range(1,N+1):
    sum_ans += i * cal(factorization(i))

print(sum_ans)
"""
n = int(input())
ans = 0
for i in range(1, n + 1):
    d = n // i
    ans += i * d * (d + 1) // 2
print(ans)
