import copy
(N, M) = list(map(int, input().split()))
num_list = list(map(int, input().split()))
list1 = copy.copy(num_list)
for i in range(M):
    (A, B) = list(map(int, input().split()))
    if num_list[A - 1] < num_list[B - 1]:
        list1[A - 1] = 0
    elif num_list[A - 1] > num_list[B - 1]:
        list1[B - 1] = 0
    else:
        list1[A - 1] = 0
        list1[B - 1] = 0
s = 0
for j in list1:
    if j > 0:
        s = s + 1
print(s)
