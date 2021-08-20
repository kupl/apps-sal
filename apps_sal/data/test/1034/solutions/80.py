from heapq import heappop, heappush
(X, Y, Z, K) = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
a_list.sort(reverse=True)
b_list.sort(reverse=True)
c_list.sort(reverse=True)
h = []
a = a_list[0]
b = b_list[0]
c = c_list[0]
heappush(h, (-(a + b + c), 0, 0, 0))
key_dict = dict()
key_dict[0, 0, 0] = 1
ans_list = []
for i in range(K):
    (ans, a, b, c) = heappop(h)
    ans_list.append(-ans)
    a1 = (a + 1, b, c)
    b1 = (a, b + 1, c)
    c1 = (a, b, c + 1)
    if a + 1 < X and (not a1 in key_dict):
        heappush(h, (-(a_list[a + 1] + b_list[b] + c_list[c]), a + 1, b, c))
        key_dict[a + 1, b, c] = 1
    if b + 1 < Y and (not b1 in key_dict):
        heappush(h, (-(a_list[a] + b_list[b + 1] + c_list[c]), a, b + 1, c))
        key_dict[a, b + 1, c] = 1
    if c + 1 < Z and (not c1 in key_dict):
        heappush(h, (-(a_list[a] + b_list[b] + c_list[c + 1]), a, b, c + 1))
        key_dict[a, b, c + 1] = 1
for ans in ans_list:
    print(ans)
