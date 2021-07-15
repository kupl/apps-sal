n = int(input())
mas = list(map(int, input().split()))
dict1 = dict()
for i in range(len(mas)):
    dict1[mas[i]] = i
min_dict1 = dict1[mas[0]]
min_ans = mas[0]
for i in dict1:
    if dict1[i] < min_dict1:
        min_dict1 = dict1[i]
        min_ans = i
print(min_ans)
