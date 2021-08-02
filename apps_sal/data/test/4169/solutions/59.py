N, M = map(int, input().split())
list1 = []
cost = 0
for i in range(N):
    A, B = map(int, input().split())
    list1.append((A, B))
list2 = sorted(list1, key=lambda x: x[0])
for i in range(N):
    if M >= list2[i][1]:
        M -= list2[i][1]
        cost += list2[i][0] * list2[i][1]
    else:
        break
cost += list2[i][0] * M
print(cost)
