N = int(input())
a = list(map(int, input().split()))
edge_list = list(a)
edge_list.sort(reverse=True)
longest_edge = edge_list.pop(0)
left_sum = 0
for i in edge_list:
    left_sum += i
if longest_edge < left_sum:
    print('Yes')
else:
    print('No')
