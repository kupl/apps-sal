import sys
n, t = list(map(int,sys.stdin.readline().split()))
x = sys.stdin.readline()
y = x.find('.')
for i in range(y+1,n):
    if x[i] > '4':
        for j in range(t):
            i -= 1
            if x[i] != '4': break
        if i == y:
            i -= 1
            while i and x[i] == '9':
                i -= 1
            x = x[:i] + str(int(x[i]) + 1) + '0' * (y - i - 1)
        else:
            x = x[:i] + str(int(x[i]) + 1)
        break
print(x)

    


