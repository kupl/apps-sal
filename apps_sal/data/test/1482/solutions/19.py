arr = input().split()
n = int(arr[0])
k = int(arr[1])
arr = input().split()
s = set()
for ch in arr:
    s.add(int(ch))
for ch in arr:
    print(ch, end=' ')
    ctr = 0
    ptr = 1
    while ctr < n - 1:
        if ptr not in s:
            print(str(ptr), end=' ')
            ctr += 1
            s.add(ptr)
        ptr += 1
    print('')
