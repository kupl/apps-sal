n,z,w = map(int,input().split())
a = [int(i) for i in input().split()]

if n == 1:
    print(abs(w-a[0]))
    return

print(max(abs(w-a[n-1]),abs(a[n-1]-a[n-2])))
