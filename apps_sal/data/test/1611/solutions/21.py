n = int(input())
arr = []
sum = 0
for x in input().split():
    arr.append(int(x))
    sum += int(x)

ln = 0
for i in range(0, len(arr)):
    if(ln<arr[i]):
        ln = arr[i]

sn = sum - ln

print(str(ln-sn+1))
