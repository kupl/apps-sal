n = int(input())
arr = input()
arr = arr + ' ' + arr
k = 0
maxx = 0
for i in arr.split():
    if i == '1':
        k += 1
        maxx = max(k, maxx)
    else:
        k = 0
print(maxx)
