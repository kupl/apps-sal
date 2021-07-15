N, M, X = map(int,input().split())
fee = list(map(int,input().split()))
result_1 = []
result_2 = []

for i in fee:
    if i > X:
        result_1.append(i)
    else:
        result_2.append(i)

result = (min(len(result_1) ,len(result_2)))
print(result)
