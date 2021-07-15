n = int(input())
l = list(map(int, input().split()))
while l != list(sorted(l)):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            print(i+1, i+2)

