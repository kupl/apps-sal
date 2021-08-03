def minimum(l):
    min_value = l[0]
    min_index = 0
    for i in range(1, len(l)):
        if l[i] < min_value:
            min_value = l[i]
            min_index = i
    return min_value, min_index


n, k = [int(s) for s in input().split()]
needs = [int(s) for s in input().split()]
has = [int(s) for s in input().split()]
can_bake = [int(has[i] / needs[i]) for i in range(n)]
# print(can_bake)
while k > 0:
    min_value, min_index = minimum(can_bake)
    has[min_index] += 1
    k -= 1
    can_bake[min_index] = int(has[min_index] / needs[min_index])
print(min(can_bake))
