def solve(printing):
    n = int(input())
    nums = [int(st) - 1 for st in input().split(' ')]
    numdupe = [0] * n
    dupeindex = []
    dupeindexindv = {}
    missing = []
    if printing:
        print('nums')
        print(nums)
    for i in range(n):
        numdupe[nums[i]] += 1
    for i in range(n):
        if numdupe[i] == 0:
            missing.append(i)
        if numdupe[nums[i]] >= 2:
            dupeindex.append(i)
            if nums[i] in dupeindexindv:
                dupeindexindv[nums[i]][1].append(i)
            else:
                dupeindexindv[nums[i]] = [0, [i], False]
    for num in dupeindexindv:
        dupeindexindv[num][0] = len(dupeindexindv[num][1])
    if printing:
        print('missing')
        print(missing)
        print('dupeindexindv')
        print(dupeindexindv)
    misslen = len(missing)
    misindex = 0
    for index in dupeindex:
        if misslen <= misindex:
            break
        elif dupeindexindv[nums[index]][0] == 1 and (not dupeindexindv[nums[index]][2]):
            dupeindexindv[nums[index]][0] -= 1
            dupeindexindv[nums[index]][2] = True
        elif dupeindexindv[nums[index]][0] > 0:
            if dupeindexindv[nums[index]][2] or missing[misindex] < nums[index]:
                dupeindexindv[nums[index]][0] -= 1
                nums[index] = missing[misindex]
                misindex += 1
            else:
                dupeindexindv[nums[index]][0] -= 1
                dupeindexindv[nums[index]][2] = True
    print(misslen)
    for num in nums:
        print(num + 1, end=' ')


solve(False)
