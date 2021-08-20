my_string = input().strip()
my_string = list(my_string)
sl = len(my_string)
m = int(input())
for i in range(m):
    (l, r, k) = list(map(int, input().split()))
    range_length = r - l + 1
    k = k % range_length
    l = l - 1
    k = range_length - k
    my_string[l:r] = my_string[l + k:r] + my_string[l:l + k]
ans = ''.join(my_string)
print(ans)
