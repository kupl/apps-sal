n = int(input())
arr = []
for _ in range(n):
    d1,d2 = input().split()
    if d1==d2:
        arr.append(True)
    else:
        arr.append(False)
for i in range(n-2):
    if arr[i] and arr[i+1] and arr[i+2]:
        print('Yes')
        break
else:
    print('No')
