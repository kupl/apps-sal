n, s = map(int, input().split())

arr = [int(x) for x in input().split()]

arr.sort()

#print(n, s, arr)

#print(sum(arr[:-1]))

if sum(arr[:-1]) <= s:
    print("YES")
else: print("NO")
