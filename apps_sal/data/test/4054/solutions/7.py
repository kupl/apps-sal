a = [1,1,2,7,4]
b = list(map(int, input().split()))
m = 1000
for i in range(5):
    m = min(b[i]//a[i],m)
print(m)
