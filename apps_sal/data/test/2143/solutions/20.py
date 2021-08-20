def find_sum_of_two(a, n):
    d = dict()
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
    return max(d.values())


n = int(input())
a = [int(x) for x in input().split()]
print(find_sum_of_two(a, n))
