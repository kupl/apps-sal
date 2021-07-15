n = int(input())

a = list(map(int, input().split()))

def f(x):
    cnt = 0
    while True:
        if x == 1:
            cnt += 1
            break
        elif x % 2 == 1:
            cnt += 1
            x = (x-1)/2
        else:
            x = x/2
    return cnt

my_dict = {}

for i in range(n):
    d = f(a[i])
    if d in my_dict.keys():
        my_dict[d] += 1
    else:
        my_dict[d] = 1



result = 0
for key in my_dict.keys():
    t = my_dict[key]
    result += int(t*(t-1)/2)

print(result)
