n = int(input())

dic = {}

for x in range(n):
    a = input()
    dic.setdefault(a, 0)
    dic[a] += 1

dic2 = sorted(list(dic.items()), key=lambda x: x[1], reverse=True)

max_word = [k for k, v in dic2 if v == dic2[0][1]]

max_word.sort()

for x in max_word:
    print(x)
