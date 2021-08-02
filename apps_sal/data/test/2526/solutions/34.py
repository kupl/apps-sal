import heapq
x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

x_tmp = P[:x]
y_tmp = Q[:y]

tmp_li = x_tmp + y_tmp
heapq.heapify(tmp_li)

for i in range(c):
    if R[i] > tmp_li[0]:
        heapq.heapreplace(tmp_li, R[i])
print(sum(tmp_li))
