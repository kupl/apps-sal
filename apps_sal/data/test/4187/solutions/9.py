# # Soru 1
#
# nm = list(map(int, input().split()))
# n = nm[0]
# m = nm[1]
#
# if int(m/n) != m/n:
#     print(-1)
# elif m/n == 1:
#     print(0)
# else:
#     x = m//n
#     count = 0
#     while x%2 == 0:
#         x = x//2
#         count += 1
#     while x%3 == 0:
#         x = x//3
#         count += 1
#     if x != 1:
#         print(-1)
#     else:
#         print(count)
# Soru 2
n = int(input())
lst = list(map(int, input().split()))
lst = lst + lst
count = 0
large = 0
for i in lst:
    if i == 1:
        count += 1
    else:
        if count > large:
            large = count
        count = 0
print(large)



