def cek(arr):
    maxx = 0
    for i in range(len(arr) - 1):
        kurang = int(arr[i + 1]) - int(arr[i])
        if kurang > maxx:
            maxx = kurang
    return maxx


n = int(input())
arr = [0] * n
b = input().split(" ")
for i in range(n):
    arr[i] = int(b[i])
narr = len(arr)
ign = 0
minn = 9999
for i in range(narr - 2):
    ign += 1
    kan = []
    for j in range(narr):
        if j == ign:
            continue
        else:
            kan += [arr[j]]
    hasil = cek(kan)
    if hasil < minn:
        minn = hasil

print(minn)
