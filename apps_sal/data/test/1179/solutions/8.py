def solve(n, k):
    tmp = 0
    i = 0
    while tmp < k:
        i += 1
        tmp += i
    tmp -= i
    return k - tmp - 1


data = input().split()
data2 = input().split()
ind = solve(int(data[0]), int(data[1]))
print(data2[ind])
