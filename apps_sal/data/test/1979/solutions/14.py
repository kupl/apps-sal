from sys import stdin
input = stdin.readline
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
elt_to_pos1 = [0] * n
elt_to_pos2 = [0] * n
for i in range(n):
    elt_to_pos1[l1[i] - 1] = i
    elt_to_pos2[l2[i] - 1] = i
dupa = [0] * n
for i in range(n):
    if elt_to_pos1[i] <= elt_to_pos2[i]:
        dupa[elt_to_pos2[i] - elt_to_pos1[i]] += 1
    else:
        dupa[n - elt_to_pos1[i] + elt_to_pos2[i]] += 1
print(max(dupa))
