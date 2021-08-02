def solve(printing):

    n = int(input())
    nums = [int(st) - 1 for st in input().split(" ")]
    numdupe = [0] * n
    dupeindex = []
    dupeindexindv = {}
    missing = []

    if printing:
        print("nums")
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
                # left location, dupe indexs, if already located original

    for num in dupeindexindv:
        dupeindexindv[num][0] = len(dupeindexindv[num][1])

    if printing:
        print("missing")
        print(missing)
        print("dupeindexindv")
        print(dupeindexindv)

    misslen = len(missing)
    misindex = 0
    #answer = 0
    for index in dupeindex:

        if misslen <= misindex:
            break

        elif dupeindexindv[nums[index]][0] == 1 and not dupeindexindv[nums[index]][2]:
            # one spot left but original not located yet.
            # locate original.
            dupeindexindv[nums[index]][0] -= 1
            dupeindexindv[nums[index]][2] = True

        elif dupeindexindv[nums[index]][0] > 0:

            if dupeindexindv[nums[index]][2] or missing[misindex] < nums[index]:
                # num is smaller or original is already located.
                # locate missing number.
                dupeindexindv[nums[index]][0] -= 1
                nums[index] = missing[misindex]
                misindex += 1
                #answer += 1

            else:  # locate original
                dupeindexindv[nums[index]][0] -= 1
                dupeindexindv[nums[index]][2] = True

    print(misslen)
    for num in nums:
        print(num + 1, end=" ")


solve(False)
