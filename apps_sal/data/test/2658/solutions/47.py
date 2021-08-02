N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
list_town = []
set_town = set()
town = 1

for i, v in enumerate(A):
    dic[i + 1] = v

for _ in range(K):
    list_town.append(town)
    set_town.add(town)
    town = dic[town]
    if town in set_town:
        stop_town = town
        break

if N <= K:
    list_first_split = list_town[:list_town.index(stop_town)]
    list_second_split = list_town[list_town.index(stop_town):]
    print(list_second_split[(K - (len(list_first_split))) % len(list_second_split)])
else:
    print(town)
