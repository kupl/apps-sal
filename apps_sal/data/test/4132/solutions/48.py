n = int(input())
a = list(map(int,input().split()))

a.sort()

def mod():
    for i in range(1, len(a)):
        # print("--------")
        # print(a[i])
        # print(a[i] % a[0])
        # print("--------")
        if(a[i] % a[0] != 0):
            a[i] = a[i] % a[0]
        else:
            a[i] = a[0]
        # print(a[i])
    a.sort()
    return a

# for i in range(4):
#     a = mod()
#     print(a)

while(a.count(a[0]) != len(a)):
    a = mod()
    # print(a)

print(a[0])
