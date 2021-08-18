n, k, l = list(map(int, input().split()))
m = n * k
arr = list(map(int, input().split()))
arr.sort(reverse=True)
# print(arr)
min_elem = arr[m - 1]
r = min_elem + l
#print("m =", m, "r =", r, arr[m - n])
if arr[m - n] > r:
    # print("печаль")
    print("0")
    return
volume = 0
if k == 1:
    for i in range(m):
        volume = volume + arr[i]
    print(volume)
    return
########

index = 0
while arr[index] > r:
    index += 1
volume = 0
# print(index)
q = index // (k - 1)
w = index % (k - 1)
while q != 0:
    volume = volume + arr[index]
    q -= 1
    index += 1
w = k - 1 - w
index += w
while index < m:
    volume = volume + arr[index]
    index += k

# print(index)
print(volume)
