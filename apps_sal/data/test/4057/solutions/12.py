n = int(input())
a = [int(c) for c in input().split(' ')]
dic = {}
for num in a:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1
print(max((dic[num] for num in dic)))
