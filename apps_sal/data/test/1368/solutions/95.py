import sys
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n,a,b = map(int,input().split())
v_list = list(map(int,input().split()))

v_list.sort(reverse=True)
max_mean = sum(v_list[:a])/a

number = v_list[a-1]

if v_list[:a].count(number) == a:
    count = 0
    for i in range(a,b+1):
        rest_list = v_list[i:]
        all_num = v_list.count(number)
        rest_num = rest_list.count(number)
        if rest_num > 0 or v_list[i-1] == number:
            count += comb(all_num,rest_num)
    print(max_mean)
    print(count)
else:
    rest_list = v_list[a:]
    all_num = v_list.count(number)
    rest_num = rest_list.count(number)
    print(max_mean)
    print(comb(all_num,rest_num))
