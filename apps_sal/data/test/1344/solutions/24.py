n = int(input())
a = list(map(int, input().split()))

maxx = 1
my_max = 1

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        maxx += 1
        if maxx > my_max:
            my_max = maxx
    else:
        if maxx > my_max:
            my_max = maxx
        maxx = 1
        

print(my_max)
