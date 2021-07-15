import math
from itertools import accumulate

# エラトステネスの篩
def eratosthenes(n): 
    prime_list = []
    num_list=[i for i in range(2, n+1)] # 2以上n以下の整数を並べる
    limit = math.sqrt(n)
    while True:
        if limit <= num_list[0]:
            return prime_list + num_list
        prime_list.append(num_list[0])
        num_list = [e for e in num_list if e % num_list[0] != 0] # 倍数をふるい落とす

max_lr = 100000
er_list = eratosthenes(max_lr)

count = [0] * max_lr
for i in range(len(er_list)):
    if (er_list[i]+1)//2 in er_list:
        count[er_list[i]] = 1

# 累積和            
count = list(accumulate(count)) 

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(count[r]-count[l-1])
