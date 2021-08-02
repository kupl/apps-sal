n = int(input())
l = [-1] + list(map(int, input().split()))
for i in range(1, n + 1):
    x = [0] * (n + 1)
    x[i] += 1
    z = i
    while(1):
        x[l[z]] += 1
        if(x[l[z]] == 2):
            print(l[z], end=' ')
            break
        z = l[z]
