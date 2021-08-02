n = int(input())
weights = list(map(int, input().split()))

mylist = []

for i in range(n):
    s1_sum = sum(weights[0:i])
    s2_sum = sum(weights[i:n])
    mylist.append(abs(s1_sum - s2_sum))

print(min(mylist))
