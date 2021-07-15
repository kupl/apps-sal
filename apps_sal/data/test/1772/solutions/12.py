# import sys
#
# ans = []
# for line in sys.stdin:
#     temp = line.split('\t')
#     tmp = temp[0][:7] + '.'*(80 - len(temp[-1]) - 7) + temp[-1].strip('\n')
#     ans.append(tmp)
# print('\n'.join(ans))

n = int(input())
a = list(map(int, input().split()))
odd = 0
even = 0
for i in a:
    if i % 2 != 0:
        odd += 1
    else:
        even += 1
if odd <= even:
    print(min(odd, even))
else:
    diff = odd - even
    print(min(odd, even) + diff // 3)

