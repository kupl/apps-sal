N = input()
Nums = list(map(int, input().split()))
result = 0
for i in Nums:
    for ii in Nums:
        if result < abs(i - ii):
            result = abs(i - ii)
print(result)
