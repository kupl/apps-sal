n = int(input())
s = list(map(int, input().split()))
q = int(input())
l = []
candies = 0
r = []

for _ in range(q):
    lr = input().split()
    l.append(int(lr[0]))
    r.append(int(lr[1]))

# for i in range(q):
#     new_array = s[l[i] - 1:r[i]]
#     while len(new_array) != 1:
#         j = 0
#         new_array1 = []
#         while j < len(new_array):
#             if new_array[j] + new_array[j+1] >= 10:
#                 candies += 1
#             new_array1.append((new_array[j] + new_array[j+1]) % 10)
#             j += 2
#         new_array = new_array1
#     print(candies)
#     candies = 0
sum_array = [0]
sum_total = 0

for j in s:
    sum_total += j
    sum_array.append(sum_total)

for i in range(q):
    total = sum_array[r[i]] - sum_array[l[i] - 1]
    candies = total // 10
    print(candies)
