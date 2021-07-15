n = int(input())
a = [int(x) for x in input().split()]
diff = (n - a[0]) % n
for i in range(1, n):
    if i % 2 == 0:
        if (a[i] + diff) % n != i:
            #print((a[i] - diff) % n, i)
            print("No")
            return
    else:
        if (a[i] - diff) % n != i:
            #print((a[i] - diff) % n, i)
            print("No")
            return
print("Yes")

