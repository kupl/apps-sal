n, m = (int(i) for i in input().split())
numbers = [int(i) for i in input().split()]
results = {0}

res_update = results.update

for i in numbers:
    tmp_results = set()
    for j in results:
        if (j+i) % m == 0:
            print('YES')
            return
        tmp_results.add((j+i) % m)
    res_update(tmp_results)
print('NO')



