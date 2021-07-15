n = int(input())
a = list(map(int, input().split()))
a.sort()
fir = a.count(a[0])
sec = a.count(a[1])
th = a.count(a[2])
if a[0] == a[1] and a[1] == a[2]:
    print(fir * (fir - 1) * (fir - 2) // 6)
elif a[0] == a[1]:
    print(fir * (fir - 1) // 2 * th)
elif a[1] == a[2]:
    print(fir * sec * (sec - 1) // 2)
else:
    print(fir * sec * th)
    

