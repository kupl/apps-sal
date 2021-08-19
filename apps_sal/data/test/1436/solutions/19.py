n = int(input())
a = input().split()
a = [int(i) for i in a]
l = 0
k = 0
for i in a:
    if i == -1:
        if l < 1:
            k += 1
        else:
            l -= 1
    else:
        l += i
print(k)
