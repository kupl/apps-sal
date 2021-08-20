N = int(input())
(T, A) = list(map(int, input().split()))
temp_list = list(map(int, input().split()))
near_place = 100000
H = []
min_index = 0
for i in range(N):
    a = T - temp_list[i] * 0.006
    H.append(abs(A - a))
print(H.index(min(H)) + 1)
