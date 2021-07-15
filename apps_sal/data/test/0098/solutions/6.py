a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
for i in range(2):
    for j in range(2):
        if min(b[i] + c[j], max(b[1 - i], c[1 - j])) <= a[0] and max((b[i] + c[j],  max(b[1 - i], c[1 - j]))) <= a[1]:
            print("YES")
            return
        #print(b[i] + c[j], max(b[1 - i], c[1 - j]))
print("NO")
            

