K, X = map(int, input().split())
num_list = []

for i in range(1, K):
    num_list.append(X + i)
    num_list.append(X - i)
num_list.append(X)
num_list.sort()

result_list = []
for n in num_list:
    num = str(n)
    result_list.append(num)
print(" ".join(result_list))
