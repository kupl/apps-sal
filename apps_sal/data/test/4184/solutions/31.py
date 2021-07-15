weight_number = int(input())
weight = list(map(int, input().split()))
difference = []
for i in range(weight_number):
    difference.append(abs(sum(weight[:i]) - sum(weight[i:])))
print(min(difference))
