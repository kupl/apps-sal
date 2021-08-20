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
sum_array = [0]
sum_total = 0
for j in s:
    sum_total += j
    sum_array.append(sum_total)
for i in range(q):
    total = sum_array[r[i]] - sum_array[l[i] - 1]
    candies = total // 10
    print(candies)
