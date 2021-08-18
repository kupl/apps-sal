from heapq import heappop, heappush

X, Y, Z, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a_list.sort(reverse=True)
b_list.sort(reverse=True)
c_list.sort(reverse=True)

hq = []

arg_hash = {}

val = -(a_list[0] + b_list[0] + c_list[0])
heappush(hq, (val, 0, 0, 0))

ans_arr = []

for i in range(K):
    ans_val, p, q, r = heappop(hq)
    ans_arr.append(-ans_val)

    arg_a = (p + 1, q, r)
    arg_b = (p, q + 1, r)
    arg_c = (p, q, r + 1)

    if (p < X - 1) and (arg_a not in arg_hash):
        arg_hash[arg_a] = 1
        heappush(hq, (-(a_list[p + 1] + b_list[q] + c_list[r]), ) + arg_a)
    if (q < Y - 1) and (arg_b not in arg_hash):
        arg_hash[arg_b] = 1
        heappush(hq, (-(a_list[p] + b_list[q + 1] + c_list[r]), ) + arg_b)
    if (r < Z - 1) and (arg_c not in arg_hash):
        arg_hash[arg_c] = 1
        heappush(hq, (-(a_list[p] + b_list[q] + c_list[r + 1]), ) + arg_c)

for i in range(len(ans_arr)):
    print((ans_arr[i]))
