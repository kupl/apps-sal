import heapq
from collections import deque
(must_red, must_green, a, b, c) = list(map(int, input().split()))
delicious_red_ls = list(map(int, input().split()))
delicious_green_ls = list(map(int, input().split()))
delicious_free_ls = list(map(int, input().split()))
delicious_red_ls.sort(reverse=True)
delicious_green_ls.sort(reverse=True)
first_red = delicious_red_ls[:must_red]
first_green = delicious_green_ls[:must_green]
first_set = first_green + first_red
first_set.sort()
delicious_free_ls.sort()
while delicious_free_ls:
    to_be_erased = heapq.heappop(first_set)
    erase = delicious_free_ls[-1]
    if to_be_erased < erase:
        new = delicious_free_ls.pop()
        heapq.heappush(first_set, new)
    else:
        heapq.heappush(first_set, to_be_erased)
        break
print(sum(first_set))
