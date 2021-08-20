values_nr = int(input())
idx___value = [int(x) for x in input().split()]
if len(idx___value) % 2 != 0 and idx___value[0] % 2 != 0 and (idx___value[-1] % 2 != 0):
    print('Yes')
else:
    print('No')
