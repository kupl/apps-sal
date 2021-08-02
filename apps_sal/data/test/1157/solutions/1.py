n = int(input())
l1 = list(map(int, input().split()))
negative = 0
total = n * (n + 1) // 2
negative_till = 0
positive_till = 0
for item in l1:
    if item > 0:
        positive_till += 1
    else:
        temp = positive_till
        positive_till = negative_till
        negative_till = temp + 1
    negative += negative_till
print(negative, total - negative)
