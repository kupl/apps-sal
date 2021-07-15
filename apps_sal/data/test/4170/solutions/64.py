n = int(input())
h = list(map(int,input().split()))
num,num_max = 0,0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        num += 1
    else:
        num = 0
    if num > num_max:
        num_max = num
print(num_max)
