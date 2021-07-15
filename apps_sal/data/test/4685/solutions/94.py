list_abc = sorted([int(i) for i in input().split()])
k = int(input())
print(list_abc[2] * 2 ** k + sum(list_abc[:2]))
