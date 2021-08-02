# Bismillahirahmanirahim
# Soru 1
#
# nv = list(map(int, input().split()))
#
# n = nv[0] - 1
# v = nv[1]
# if v >= n:
#     print(n)
#     quit()
# k = 2
# money = v
# while n - v > 0:
#     n = n - 1
#     money += k
#     k += 1
# print(money)

# Soru2
def carpan(n):
    lst = []
    sq = n**0.5 + 1
    for i in range(2, int(sq) + 1):
        if n % i == 0:
            lst.append(i)
    return lst


n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)
mn = lst[-1]
total = sum(lst)
large = 0
for i in lst:
    mx = i
    lst1 = carpan(mx)
    for j in lst1:
        if mx + mn - (mx / j + mn * j) > large:
            large = mx + mn - (mx / j + mn * j)
print(int(total - large))
