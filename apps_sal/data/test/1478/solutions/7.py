from collections import defaultdict


def ri():
    return list(map(int, input().split()))


temp = input().split(',')
node = temp[0::2]
count = temp[1::2]
count = list(map(int, count))
level = defaultdict(list)
stack = []
l = 0
for j in range(len(node)):
    level[l].append(j)
    if count[j]:
        count[j] -= 1
        stack.append(j)
        l += 1
    else:
        while len(stack):
            if count[stack[-1]] == 0:
                stack.pop()
                l -= 1
            else:
                count[stack[-1]] -= 1
                break
print(len(level))
for l in level:
    print(' '.join([node[i] for i in level[l]]))
