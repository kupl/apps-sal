N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for i, v in enumerate(A):
    dic[i + 1] = v

town = 1
s = set()
l = []
for _ in range(K):
    l.append(town)
    s.add(town)
    town = dic[town]
    if town in s:
        stop_twon = town
        break
if N <= K:
    list_first_split = l[:l.index(stop_twon)]
    list_second_split = l[l.index(stop_twon):]
    print(list_second_split[(K - (len(list_first_split))) % len(list_second_split)])
else:
    print(town)
