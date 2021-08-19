n = int(input())
l1 = list(sorted(list(map(int, input().split()))))
l2 = list(sorted(list(map(int, input().split())))) + [-1]
l3 = list(sorted(list(map(int, input().split())))) + [-1, -1]
for i in range(n):
    if l1[i] != l2[i]:
        w = l1[i]
        break
for i in range(n):
    if l2[i] != l3[i]:
        x = l2[i]
        break
print(w)
print(x)
