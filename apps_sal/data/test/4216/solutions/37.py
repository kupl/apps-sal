import sys

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors  + upper_divisors[::-1]


input = sys.stdin.readline

n = int(input())

yaku_list = make_divisors(n)
length = len(yaku_list)
half_index = int(length/2)

a = 0
b = 0
if length % 2 == 0:
    a = yaku_list[half_index]
    b = yaku_list[half_index-1]
else:
    a = yaku_list[half_index]
    b = a

keta_a = len(str(a))
keta_b = len(str(b))

print(max(keta_a,keta_b))
