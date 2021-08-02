n = int(input())
test = list(map(int, input().split()))
test1 = []
result = []
test.sort(reverse=True)

num = test.count(test[0])

test1.append(test[0])
mark = 0

for i in range(num, len(test)):
    if test[i] != test1[len(test1) - 1]:
        test1.append(test[i])
        mark = 0
    else:
        if mark > 0:
            continue
        else:
            test1.append(test[i])
            mark += 1

result.append(test1[0])
for j in range(1, len(test1)):
    if test1[j] != result[len(result) - 1]:
        result.append(test1[j])
    else:
        result.insert(0, test1[j])
print(len(result))
print(' '.join(map(str, result)))
