n = int(input())
data = input()
answer = 0
for i in range(n):
    for j in range(n):
        if i <= j:
            help = data[i:j + 1]
            L = help.count('L')
            R = help.count('R')
            U = help.count('U')
            D = help.count('D')
            if L == R and U == D:
                answer += 1
print(answer)
