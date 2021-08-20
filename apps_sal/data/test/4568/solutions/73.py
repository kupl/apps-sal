n = int(input())
s = input()
list_intersection = []
for i in range(1, n + 1):
    a = set(s[:i])
    b = set(s[i:])
    intersection_a_b = a.intersection(b)
    list_intersection.append(len(intersection_a_b))
print(max(list_intersection))
