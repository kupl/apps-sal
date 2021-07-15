n = int(input())
lst = list(enumerate(list(map(int, input().split()))))
 
sorted_lst = sorted(lst, key = lambda x: x[1])
left_next_index = list(range(-1, n - 1)) + [-1, -1]
right_next_index = list(range(1, n + 1)) + [n, n]
 
ans = 0
for i, p in sorted_lst:
    l2 = left_next_index[i]
    l1 = left_next_index[l2]
    r1 = right_next_index[i]
    r2 = right_next_index[r1]
    
    a = p * ((l2 - l1) * (r1 - i) + (r2 - r1) * (i - l2))
    ans += a
    
    left_next_index[r1] = l2
    right_next_index[l2] = r1
print(ans)
