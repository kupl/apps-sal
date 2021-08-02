import math
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def calc_ans(k, a, b):
    div = (10**k - 1) // a + 1

    b_min = b * 10**(k - 1)
    b_max = (b + 1) * 10**(k - 1) - 1

    d_min_inc = math.ceil(b_min / a)
    d_max_inc = math.floor(b_max / a)
    # if d_min_inc*a > b_max:
    # 	return div
    # else:

    # print (k,a,b,div,div - (d_max_inc - d_min_inc + 1))

    return div - (d_max_inc - d_min_inc + 1)


p = 10**9 + 7

ans = 1
for ai, bi in zip(a, b):
    ans = (ans * calc_ans(k, ai, bi)) % p

print(ans)


def easy_calc(k, a, b):
    ans = 0
    for i in range(10**k):
        c = str(i)
        first = int(c[0]) if len(c) == k else 0
        if i % a == 0 and not first == b:
            ans += 1
    return ans

# import random
# for i in range(100):
# 	k = random.randrange(4,5)
# 	a = random.randrange(1,10**k)
# 	b = random.randrange(0, 10)
# 	if easy_calc(k,a,b) != calc_ans(k,a,b):
# 		print(k,a,b, easy_calc(k,a,b), calc_ans(k,a,b))
# 		1/0
