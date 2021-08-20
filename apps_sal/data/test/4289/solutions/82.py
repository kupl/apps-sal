def ave_ten(T, x):
    return T - x * 0.006


N = int(input())
(T, A) = map(int, input().split())
li = list(map(int, input().split()))
min_ten = 9999999999
for i in range(len(li)):
    if abs(min_ten - A) > abs(ave_ten(T, li[i]) - A):
        min_ten = ave_ten(T, li[i])
        min_in = i + 1
print(min_in)
