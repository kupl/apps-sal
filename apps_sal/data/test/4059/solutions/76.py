n = int(input())
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
# cnt=0
# for c in range(1,n):
#     ab = n-c
#     ls = make_divisors(ab)
#     cnt+=len(ls)
# print(cnt, flush=True)

# C will be decided automatically
cnt=0
for a in range(1,n):
    b = (n-1)//a
    cnt += b
print(cnt, flush=True)


